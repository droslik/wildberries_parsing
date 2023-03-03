from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GoodsSerializer
from .utils import input_data_processing


class GoodsApiView(APIView):
    """
    Class for representation of goods to be received upon request-parsing
    """

    serializer_class = GoodsSerializer

    def post(self, request):
        data = input_data_processing(request)
        if isinstance(data, list):
            serializer = self.serializer_class(
                data, context={"request": request}, many=True
            )
            return Response(serializer.data)
        return Response(self.serializer_class(data).data)
