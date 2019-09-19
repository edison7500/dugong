import logging

from rest_framework import serializers
from .models import Post

# from taggit_serializer.serializers import TaggitSerializer
# from apps.ext.rest.serializers.taggit import TaggitListSerializerField

logger = logging.getLogger("django")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ["id"]
