import logging

from rest_framework import serializers

# from taggit_serializer.serializers import (
#     TagListSerializerField,
#     TaggitSerializer,
# )

from .models import Post

logger = logging.getLogger("django")


class PostSerializer(serializers.ModelSerializer):
    digest = serializers.CharField()
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

    def get_tags(self, obj) -> list:
        return [
            {"id": tag.id, "name": tag.name, "slug": tag.slug}
            for tag in obj.tags.all()
        ]
