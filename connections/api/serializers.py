from rest_framework import serializers


class ConnectionSerializer(serializers.Serializer):
    url = serializers.URLField()
    username = serializers.CharField()
    passowrd = serializers.CharField()
