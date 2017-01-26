from django.conf.urls import url
from books.views.api import BookListAPIView, BookDetailAPIView


urlpatterns =[
    url(r'^$', BookListAPIView.as_view(), name='book-list'),
    url(r'^(?P<asin>[0-9a-zA-Z_-]+)/?$', BookDetailAPIView.as_view(), name='book-detail'),
]