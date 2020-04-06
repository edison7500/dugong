from django.urls import path
from apps.photos.views import PhotoListView


urlpatterns = [
    path("", PhotoListView.as_view(), name="index"),
]


app_name = "photos"
