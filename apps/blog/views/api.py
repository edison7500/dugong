from rest_framework import generics
from ..models import Post
from ..serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.published()
    serializer_class = PostSerializer
