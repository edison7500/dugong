from rest_framework import generics
from rest_framework import permissions

from apps.books.models import Book
from apps.books.serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "slug"


class BookCheckAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAdminUser
    ]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "identified"
