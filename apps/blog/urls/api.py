from django.urls import path

from ..views.api import PostListAPIView, PostDetailAPIView

app_name = "blog"

urlpatterns = [
    path("", PostListAPIView.as_view(), name="index"),
    path("<slug:slug>/", PostDetailAPIView.as_view(), name="detail")
]