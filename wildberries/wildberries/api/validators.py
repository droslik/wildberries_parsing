from rest_framework import serializers


def validate_input(request):
    """
    Validates input data: file and article
    """
    file = request.FILES.get("file")
    article = request.data["article"]
    if file and article or not file and not article:
        raise serializers.ValidationError(
            "Please choose at least and at most one option: enter"
            " a valid digital article or attach the xlsx-file"
        )
    if not file and not article[0].isdigit():
        raise serializers.ValidationError(
            "Article count not contain chars or any special symbols"
        )
    return file or article
