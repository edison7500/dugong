from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("posts/", include("apps.blog.urls.api", namespace="blog")),
    path(
        "tutorials/", include("apps.tutorials.urls.api", namespace="tutorials")
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
