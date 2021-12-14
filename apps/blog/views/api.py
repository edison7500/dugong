# from rest_framework import generics
# from ..models import Post
# from ..serializers import PostSerializer
#
#
# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.published()
#     serializer_class = PostSerializer
#
#
# class PostDetailAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.published()
#     serializer_class = PostSerializer
#     lookup_field = "slug"

from rest_framework import viewsets

from apps.blog.models import Post
from apps.blog.serializers import PostSerializer


class PostAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.published()
    serializer_class = PostSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
