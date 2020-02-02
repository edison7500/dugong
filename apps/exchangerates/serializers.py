from rest_framework import serializers

from .models import ExChangeRate


class ExChangeRateSerializer(serializers.ModelSerializer):
    exchange_rates = serializers.DictField()

    class Meta:
        model = ExChangeRate
        exclude = ["id", "rates"]
