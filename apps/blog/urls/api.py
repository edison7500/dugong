from rest_framework import routers

from apps.blog.views.api import PostAPIViewSet

router = routers.SimpleRouter()

app_name = "blog"

router.register(r"", PostAPIViewSet, basename="post")

urlpatterns = router.urls
