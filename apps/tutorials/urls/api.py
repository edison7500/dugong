from rest_framework import routers
from apps.tutorials.views.api import TutorialsViewSet

router = routers.SimpleRouter()

app_name = "tutorials"

router.register(r"", TutorialsViewSet, basename="tutorials")

urlpatterns = router.urls
