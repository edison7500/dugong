from django.conf.urls import url
from apps.books.views.api import (
    BookListAPIView
)


urlpatterns = [
    url(r'^$', BookListAPIView.as_view(), name='list'),
]