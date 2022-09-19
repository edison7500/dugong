"""Urls for `toolbox` app."""

from django.urls import path  # noqa
from rest_framework.routers import SimpleRouter
from apps.toolbox.views import ToolBoxAPIViewSet

# Default app name to use for namespacing this app's URLs.
# (a template url must include `toolbox:` as a prefix to reach here).
# https://docs.djangoproject.com/en/3.2/topics/http/urls/#url-namespaces-and-included-urlconfs
app_name = "toolbox"

router = SimpleRouter()
router.register(r"", ToolBoxAPIViewSet, basename="toolbox-api")
urlpatterns = router.urls

# urlpatterns = [
#     # Standard view paths and other includes can go here!
# ]
