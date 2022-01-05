from rest_framework import viewsets

from apps.blog.models import Post
from apps.blog.serializers import PostSerializer


class PostAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.published()
    serializer_class = PostSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
