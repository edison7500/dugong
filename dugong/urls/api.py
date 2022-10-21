from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("posts/", include("apps.blog.urls.api", namespace="blog")),
    path(
        "tutorials/", include("apps.tutorials.urls.api", namespace="tutorials")
    ),
]

urlpatterns += [
    path("crypto-news/", include("apps.cryptonews.urls.api")),
    # path("toolboxes/", include("apps.toolbox.urls")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
