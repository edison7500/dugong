import logging
from rest_framework import serializers

from .models import ExChangeRate


logger = logging.getLogger("django")


class ExChangeRateSerializer(serializers.ModelSerializer):
    exchange_rates = serializers.SerializerMethodField()

    class Meta:
        model = ExChangeRate
        exclude = ["id", "rates"]

    def get_exchange_rates(self, obj) -> dict:
        _request = self.context.get("request", None)
        if _request:
            _base = _request.GET.get("base", "USD")
            return obj.exchange_rates(_base)

        return obj.exchange_rates()
