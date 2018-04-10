from rest_framework import serializers
from tutorials.models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    # images = serializers.ListField(source='get_image_urls', read_only=True)
    absolute_url = serializers.CharField(source='get_absolute_url',
                                         read_only=True)
    cover_url = serializers.URLField(source='cover', required=False, read_only=True)

    created_at = serializers.DateTimeField(source='created_datetime', required=False, read_only=True)
    # tag_list = serializers.ListField(read_only=True)

    class Meta:
        model = Tutorial
        fields = ('slug', 'cover_url', 'absolute_url',
                  'title', 'content', 'origin_link',
                  'created_at', 'published_at',)
        # exclude = ('id', 'author', 'tags')

