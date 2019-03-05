from apps.books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['id', ]
