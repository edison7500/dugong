from rest_framework import serializers
from opensource.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Project