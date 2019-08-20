from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

# from rest_framework_swagger.views import get_swagger_view
from apps.users.views.api import UserDetailsView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


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

urlpatterns = [
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=86400),
        name="schema-swagger-ui",
    ),
    url(r"^docs/$", schema_view.with_ui("redoc", cache_timeout=86400), name="schema-redoc"),
    url(r"^tutorials/", include("apps.tutorials.urls.api", namespace="tutorials")),
    # url(r"^opensource/", include("opensource.urls.api", namespace="opensource")),
    url(r"^books/", include("apps.books.urls.api", namespace="books")),
]


urlpatterns += [
    url(r"^auth/", include("rest_auth.urls")),
    url(r"^rest/profile/?$", UserDetailsView.as_view(), name="oauth_user_profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
