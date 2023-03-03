from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    """
    Class for goods representation
    """
    title = serializers.CharField(read_only=True)
    brand = serializers.CharField(read_only=True)
    article = serializers.IntegerField(read_only=False, required=False)
    file = serializers.FileField(write_only=True)
