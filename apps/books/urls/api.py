from rest_framework.routers import SimpleRouter

from apps.books.views.api import BookViewSet

router = SimpleRouter()
router.register(r'', BookViewSet, basename='books')

urlpatterns = router.urls

