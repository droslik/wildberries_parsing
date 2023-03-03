import asyncio
from io import BytesIO
from openpyxl.reader.excel import load_workbook
from rest_framework import serializers
from .services import parsing_main
from .validators import validate_input


def input_data_processing(request):
    """
    Function runs validation of input data,
    runs file reading if file is uploaded,
    runs loop with creation of tasks for parsing
    gets the results and returns it
    """
    validated_input = validate_input(request)
    if type(validated_input) is str:
        articles = [int(validated_input)]
    else:
        articles = file_reading(validated_input)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(parsing_main(articles))
    async_result = loop.run_until_complete(task)
    if async_result is not None:
        return async_result
    raise serializers.ValidationError("The results were not found")


def file_reading(validated_input):
    """
    Function runs file reading and returns list of articles
    """
    content = validated_input.read()
    wb = load_workbook(filename=BytesIO(content), data_only=True)
    articles = []
    for list_sheet in wb:
        sheet_articles = [
            int(value[0])
            for value in list_sheet.values
            if isinstance(value[0], (int, float))
        ]
        articles.extend(sheet_articles)
    return articles
