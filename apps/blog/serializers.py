import logging

from rest_framework import serializers
from .models import Post

logger = logging.getLogger("django")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ["id"]
