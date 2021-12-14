import logging

from rest_framework import serializers
from taggit_serializer.serializers import (
    TagListSerializerField,
    TaggitSerializer,
)

from .models import Post

logger = logging.getLogger("django")


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    digest = serializers.CharField()
    content = serializers.CharField()
    tags = TagListSerializerField()
    created_at_ts = serializers.IntegerField()

    class Meta:
        model = Post
        exclude = [
            "id",
        ]
