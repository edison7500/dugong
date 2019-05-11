from rest_framework import serializers
from opensource.models import (Project, Status,
                               PostProject, People, Organization, Repository)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ("created_at", "id")
        read_only_fields = ("slug",)


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        exclude = ("id",)
        read_only_fields = ('created_at',)


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        exclude = ("id", )
        read_only_fields = ('created_at',)


class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:opensource:detail',
                                               lookup_field='identified_code')

    class Meta:
        model = Project
        fields = ('url', 'id', 'author', 'name', 'desc',
                  'category', 'github_url', 'readme',)


class PostProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostProject
        fields = ('url', 'category')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('watch', 'star', 'fork', 'project', 'datetime')
