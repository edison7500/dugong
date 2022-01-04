from rest_framework import serializers

# from taggit_serializer.serializers import (
#     TagListSerializerField,
#     TaggitSerializer,
# )

from apps.tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    digest = serializers.CharField(read_only=True)
    absolute_url = serializers.CharField(
        source="get_absolute_url", read_only=True
    )
    cover_url = serializers.URLField(
        source="cover", required=False, read_only=True
    )
    created_at = serializers.DateTimeField(
        source="created_datetime", required=False, read_only=True
    )
    created_at_ts = serializers.IntegerField()

    images = serializers.SerializerMethodField(source="get_images")
    # tags = TagListSerializerField()

    class Meta:
        model = Tutorial
        fields = (
            "slug",
            "cover_url",
            "absolute_url",
            "title",
            "digest",
            "content",
            "html_content",
            "origin_link",
            "images",
            "tags",
            "created_at",
            "created_at_ts",
            "published_at",
        )

    def get_images(self, obj):
        _images = obj.images.all().values_list("file", flat=True)
        return list(_images)
