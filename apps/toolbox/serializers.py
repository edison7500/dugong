import logging
from typing import List, Dict
from rest_framework import serializers
from .models import Category
from .models import ToolBox

logger = logging.getLogger("django")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["slug", "title", "parent"]
        # exclude = ["id"]


class ToolboxSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = CategorySerializer(required=False)

    class Meta:
        model = ToolBox
        exclude = ["id"]
        # depth = 1

    def get_tags(self, obj) -> List[Dict]:
        return [{"name": tag.name, "slug": tag.slug} for tag in obj.tags.all()]
