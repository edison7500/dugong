import django_filters
from .models import Eprint


class EprintFilterSet(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Eprint
        fields = ["category"]
