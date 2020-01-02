import logging

from rest_framework import serializers
from .models import Post

logger = logging.getLogger("django")


class PostSerializer(serializers.ModelSerializer):
    html_content = serializers.CharField()
    created_at_ts = serializers.IntegerField()
    # digest = serializers.CharField()

    class Meta:
        model = Post
        exclude = ["id", "content"]
