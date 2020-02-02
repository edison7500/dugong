import logging
from rest_framework import generics
from apps.exchangerates.models import ExChangeRate
from apps.exchangerates.serializers import ExChangeRateSerializer

logger = logging.getLogger("django")


class ExChangeRateListAPIView(generics.ListAPIView):
    serializer_class = ExChangeRateSerializer

    def get_queryset(self):
        qs = ExChangeRate.objects.all()
        return qs


class ExChangeRateDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ExChangeRateSerializer
    lookup_field = "date"

    def get_queryset(self):
        qs = ExChangeRate.objects.all()
        return qs

    def get_object(self):
        _year = self.kwargs.get("year")
        _month = self.kwargs.get("month")
        _day = self.kwargs.get("day")
        _date = f"{_year}-{_month}-{_day}"
        logger.info(_date)

        qs = self.get_queryset()

        _obj = qs.get(date=_date)
        return _obj

