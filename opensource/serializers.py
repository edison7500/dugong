from rest_framework import serializers
from opensource.models import Project, Status, PostProject, Author


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('watch', 'star', 'fork', 'project', 'datetime')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author', 'url', 'created')
        read_only_fields = ('created',)


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
