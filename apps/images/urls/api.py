from django.urls import path
from apps.images.views.api import RemoveImageRimAPIView


app_name = "images"

urlpatterns = [path("remove/rim/", RemoveImageRimAPIView.as_view(), name="remove-rim")]
