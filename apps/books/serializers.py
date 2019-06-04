from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(source="tag_list")

    class Meta:
        model = Book
        exclude = ["id", "identified", "origin_link", "created_at", "updated_at"]
