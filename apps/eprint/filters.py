import django_filters
from .models import Eprint


class EprintFilterSet(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr="iexact")
    author = django_filters.CharFilter(field_name="authors", method="filter_author")
    keyword = django_filters.CharFilter(field_name="keywords", method="filter_keyword")

    def filter_author(self, queryset, name, value):
        lookup = "__".join([name, "contains"])
        return queryset.filter(**{lookup: [value]})

    def filter_keyword(self, queyset, name, value):
        lookup = "__".join([name, "contains"])
        return queyset.filter(**{lookup: [value]})

    class Meta:
        model = Eprint
        fields = ["category", "author"]
