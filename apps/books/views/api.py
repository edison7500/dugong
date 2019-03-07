from rest_framework import generics
from apps.books.serializers import BookSerializer
from apps.books.models import Book


class BookListAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
