from typing import List, Dict

from rest_framework import serializers

# from taggit_serializer.serializers import (
#     TagListSerializerField,
#     TaggitSerializer,
# )

from apps.tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    # digest = serializers.CharField(read_only=True)
    absolute_url = serializers.CharField(
        source="get_absolute_url", read_only=True
    )
    cover_url = serializers.URLField(
        source="cover", required=False, read_only=True
    )
    tags = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(
        source="created_datetime", required=False, read_only=True
    )
    created_at_ts = serializers.IntegerField()

    class Meta:
        model = Tutorial
        fields = (
            "slug",
            "cover_url",
            "absolute_url",
            "title",
            # "digest",
            "content",
            "origin_link",
            # "images",
            "tags",
            "created_at",
            "created_at_ts",
            "published_at",
        )

    def get_tags(self, obj) -> List[Dict]:
        return [{"name": tag.name, "slug": tag.slug} for tag in obj.tags.all()]
