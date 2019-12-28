from rest_framework import serializers

from apps.tutorials.models import Tutorial


# class TutorialImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ()


class TutorialSerializer(serializers.ModelSerializer):
    digest = serializers.CharField(read_only=True)
    absolute_url = serializers.CharField(source="get_absolute_url", read_only=True)
    cover_url = serializers.URLField(source="cover", required=False, read_only=True)
    created_at = serializers.DateTimeField(
        source="created_datetime", required=False, read_only=True
    )

    # images = TutorialImageSerializer(read_only=True, many=True)
    images = serializers.SerializerMethodField(source="get_images")

    class Meta:
        model = Tutorial
        fields = (
            "slug",
            "cover_url",
            "absolute_url",
            "title",
            "digest",
            "content",
            "origin_link",
            "images",
            "created_at",
            "published_at",
        )

    def get_images(self, obj):
        _images = obj.images.all().values_list("file", flat=True)
        return list(_images)
