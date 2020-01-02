import logging

from rest_framework import serializers
from .models import Post

logger = logging.getLogger("django")


class PostSerializer(serializers.ModelSerializer):
    digest = serializers.CharField()
    html_content = serializers.CharField()
    created_at_ts = serializers.IntegerField()

    class Meta:
        model = Post
        exclude = ["id", "content"]
