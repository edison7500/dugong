from rest_framework.routers import SimpleRouter
from apps.cryptonews.views.api import CryptoNewsViewSet

router = SimpleRouter()
router.register(r"", CryptoNewsViewSet, basename="crypto-news")
urlpatterns = router.urls
