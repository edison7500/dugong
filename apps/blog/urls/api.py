# from django.urls import path
#
# from ..views.api import PostListAPIView, PostDetailAPIView
#
# app_name = "blog"
#
# urlpatterns = [
#     path("", PostListAPIView.as_view(), name="index"),
#     path("<slug:slug>/", PostDetailAPIView.as_view(), name="detail"),
# ]
from rest_framework import routers

from apps.blog.views.api import PostAPIViewSet

router = routers.SimpleRouter()

app_name = "blog"

router.register(r"", PostAPIViewSet, basename="post")

urlpatterns = router.urls
