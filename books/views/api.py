# from rest_framework import viewsets
from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer


# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListAPIView(generics.ListCreateAPIView):
    model               = Book
    queryset            = Book.objects.all()
    serializer_class    = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    model               = Book
    queryset            = Book.objects.all()
    serializer_class    = BookSerializer
    lookup_field        = 'asin'




