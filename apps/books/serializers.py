import logging
from rest_framework import serializers
from .models import Book

logger = logging.getLogger("django")


class BookSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(source="tag_list")

    class Meta:
        model = Book
        exclude = ["id", "identified", "created_at", "updated_at"]
        extra_kwargs = {"origin_link": {"write_only": True}}

    def create(self, validated_data):
        tag_list = validated_data.pop("tag_list", None)
        logger.info(tag_list)
        instance = super().create(validated_data)
        for tag in tag_list:
            instance.tags.add(tag)
        return instance
