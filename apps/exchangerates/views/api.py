import logging
from rest_framework import generics
from rest_framework.generics import get_object_or_404

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
        queryset = self.filter_queryset(self.get_queryset())

        _year = self.kwargs.get("year")
        _month = self.kwargs.get("month")
        _day = self.kwargs.get("day")
        _date = f"{_year}-{_month}-{_day}"
        filter_kwargs = {self.lookup_field: _date}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj
