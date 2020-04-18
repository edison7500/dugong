from rest_framework import routers
from ..views.api import EprintSetViews

router = routers.SimpleRouter()

router.register(r"", EprintSetViews)


urlpatterns = router.urls
