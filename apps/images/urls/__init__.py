from django.conf.urls import url
from ..views import (
    ImageListView, ImageUploadView
)

urlpatterns = [
    url(r'^$', ImageListView.as_view(), name='list'),
    url(r'^upload/?$', ImageUploadView.as_view(), name='upload'),
]
