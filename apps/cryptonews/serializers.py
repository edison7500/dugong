from rest_framework import serializers
from .models import News


class CryptoNewsSerializer(serializers.ModelSerializer):
    domain = serializers.CharField(read_only=True)

    class Meta:
        model = News
        # exclude = ["id"]
        fields = "__all__"
        read_only_fields = ["id", "slug"]


class PushExchangeAnnSerializer(serializers.ModelSerializer):
    channel = serializers.CharField(
        default="ExchangeAnnChannel", read_only=True
    )

    class Meta:
        model = News
        exclude = [
            "id",
            "content",
            "slug",
        ]
