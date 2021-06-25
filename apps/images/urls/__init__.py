# from django.conf.urls import url
from django.urls import path
from ..views import ImageListView, ImageUploadView

app_name = "images"

urlpatterns = [
    path("", ImageListView.as_view(), name="list"),
    path("upload/", ImageUploadView.as_view(), name="upload"),
    # path("rim/", ImageRemoveRimView.as_view(), name="remove-rim"),
]
