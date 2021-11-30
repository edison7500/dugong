from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns

from apps.users.views.api import UserDetailsView

schema_view = get_schema_view(
    openapi.Info(
        title="Jiaxin.im API",
        default_version="v1",
        # description=" description",
        terms_of_service="https://jiaxin.im/pages/about/",
        contact=openapi.Contact(email="edison7500@gmail.com"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

app_name = "api"

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=86400),
        name="schema-swagger-ui",
    ),
    path("blog/", include("apps.blog.urls.api", namespace="blog")),
    path(
        "tutorials/", include("apps.tutorials.urls.api", namespace="tutorials")
    ),
    # path("images/", include("apps.images.urls.api", namespace="images")),
]

urlpatterns += [
    # path("auth/", include("rest_auth.urls")),
    path("o/profile/", UserDetailsView.as_view(), name="oauth_user_profile"),
    path("crypto-news/", include("apps.cryptonews.urls.api")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
