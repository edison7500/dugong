from typing import List, Dict
from rest_framework import serializers
from apps.tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(source="get_absolute_url", read_only=True)
    cover_url = serializers.URLField(
        source="cover", required=False, read_only=True
    )
    # tags = serializers.SerializerMethodField()

    created_at_ts = serializers.IntegerField()
    published_at_ts = serializers.IntegerField()

    class Meta:
        model = Tutorial
        fields = (
            "slug",
            "cover_url",
            # "url",
            "title",
            "created_at_ts",
            "published_at_ts",
        )


class TutorialDetailSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(source="get_absolute_url", read_only=True)
    cover_url = serializers.URLField(
        source="cover", required=False, read_only=True
    )
    tags = serializers.ListField(source="tag_list")

    created_at_ts = serializers.IntegerField()
    published_at_ts = serializers.IntegerField()

    class Meta:
        model = Tutorial
        fields = (
            "slug",
            "cover_url",
            # "url",
            "title",
            "content",
            "origin_link",
            "tags",
            "created_at_ts",
            "published_at_ts",
        )

    # def get_tags(self, obj) -> List[Dict]:
    #     return [{"name": tag.name, "slug": tag.slug} for tag in obj.tags.all()]
