from rest_framework import serializers
from .models import News


class CryptoNewsSerializer(serializers.ModelSerializer):
    # domain = serializers.CharField()

    class Meta:
        model = News
        exclude = ["id"]


class PushExchangeAnnSerializer(serializers.ModelSerializer):

    channel = serializers.CharField(
        default="jiaxindevchannels", read_only=True
    )

    class Meta:
        model = News
        exclude = [
            "id",
            "content",
            "slug",
        ]
