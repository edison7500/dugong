from rest_framework import serializers
from opensource.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Project
        fields  = ('author', 'name', 'desc', 'github_url', 'readme')