from django.conf.urls import url
from apps.books.views.api import BookListCreateAPIView, BookRetrieveAPIView, BookCheckAPIView

# router = SimpleRouter()
# router.register(r'', BookViewSet, basename='books')
app_name = "book"

urlpatterns = [
    url(r'^$', BookListCreateAPIView.as_view(), name='index'),
    url(r"^(?P<slug>\d+)/?$", BookRetrieveAPIView.as_view(), name="detail"),
    url(r"^(?P<identified>\w+)/check/?$", BookCheckAPIView.as_view(), name="check"),
]

