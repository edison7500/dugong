from rest_framework import serializers
from .models import News


class CryptoNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = [
            "id",
        ]
        # fields = "__all__"
