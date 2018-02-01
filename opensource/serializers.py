from rest_framework import serializers
from opensource.models import (Project, Status,
                               PostProject, People, Organization)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('watch', 'star', 'fork', 'project', 'datetime')


class OrganizationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:opensource:organization:detail',
                                               lookup_field='name')

    class Meta:
        model = Organization
        exclude = ("created_at", "id")
        # read_only_fields = ( "created_at",)


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        # fields = ('name', "bio", 'created_at')
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
