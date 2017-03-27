from rest_framework import serializers
from opensource.models import Project, Status


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Status
        fields  = ('watch', 'star', 'fork', 'project', 'datetime')


class ProjectSerializer(serializers.ModelSerializer):
    url     = serializers.HyperlinkedIdentityField(view_name='open-source-api-detail',
                                                   lookup_field='identified_code')

    class Meta:
        model   = Project
        fields  = ('url', 'id', 'author', 'name', 'desc',
                   'category', 'github_url', 'readme', )
