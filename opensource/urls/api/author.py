from django.conf.urls import url
from opensource.views.api import AuthorListAPIView


urlpatterns = [
    url(r'^$', AuthorListAPIView.as_view(), name='list'),
]