from rest_framework import serializers
from opensource.models import Project, Status


# class StatusSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model   = Status


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Project
        fields  = ('author', 'name', 'desc',
                   'github_url', 'readme')