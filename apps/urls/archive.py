from django.urls import re_path
from apps.blog.views import BlogYearArchiveView

app_name = "archive"

urlpatterns = [
    re_path(
        "^blog/(?P<year>[0-9]{4})/?$", BlogYearArchiveView.as_view(), name="blog_year"
    )
]
