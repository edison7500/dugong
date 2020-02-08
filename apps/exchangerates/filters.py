from django_filters import rest_framework as filters
from .models import ExChangeRate


class ExChangeRateFilter(filters.FilterSet):
    class Meta:
        model = ExChangeRate
        fields = ["date"]
