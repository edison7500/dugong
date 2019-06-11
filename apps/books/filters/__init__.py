import django_filters
from apps.books.models import Book


class BookFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Book.STATUS)

    class Meta:
        model = Book
        fields = ["status"]
