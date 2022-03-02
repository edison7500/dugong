import logging
from typing import List, Dict

from rest_framework import serializers

# from taggit_serializer.serializers import (
#     TagListSerializerField,
#     TaggitSerializer,
# )

from .models import Post

logger = logging.getLogger("django")


class PostSerializer(serializers.ModelSerializer):
    digest = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    created_at_ts = serializers.IntegerField()

    class Meta:
        model = Post
        exclude = [
            "id",
            "status",
            "created_at",
            "updated_at",
        ]

    def get_tags(self, obj) -> List[Dict]:
        return [{"name": tag.name, "slug": tag.slug} for tag in obj.tags.all()]

    def get_digest(self, obj) -> str:
        _digest: str = obj.digest
        _digest = _digest.replace("\n", " ")
        return f"{_digest[:100]}"
