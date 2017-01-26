from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def list(self, request, *args, **kwargs):
    #     pass

    def create(self, request, *args, **kwargs):
        print request.data['images']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)