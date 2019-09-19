from rest_framework import generics
from ..models import Post


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.published()
