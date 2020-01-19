from django.urls import path
from apps.blog.views import BlogListView, BlogDetailView, PostTagListView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="index"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="detail"),
    path("tags/<int:tid>/", PostTagListView.as_view(), name="tags"),
]
