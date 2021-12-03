from rest_framework import serializers
from .models import News


class CryptoNewsSerializer(serializers.ModelSerializer):
    # domain = serializers.CharField()
    channel = serializers.CharField(default="jiaxindevchannels")

    class Meta:
        model = News
        exclude = ["id", "slug", "content"]
