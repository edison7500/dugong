from apps.books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    cover = serializers.URLField()

    class Meta:
        model = Book
        exclude = ['id', ]
