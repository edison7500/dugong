from rest_framework import viewsets
from rest_framework import permissions
from apps.books.serializers import BookSerializer
from apps.books.models import Book


class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    lookup_field = "identified"
