from django_filters import rest_framework as filters
from .models import ExChangeRate


class ExChangeRateFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = ExChangeRate
        fields = ["date"]
