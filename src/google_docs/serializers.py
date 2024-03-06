from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=50)
