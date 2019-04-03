from rest_framework import generics
from apps.ext.rest import permissions
from apps.books.serializers import BookSerializer
from apps.books.models import Book


class BookListAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    permission_classes = [
        permissions.IsAdminOrReadOnly,
    ]
