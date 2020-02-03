from django.urls import path, re_path
from apps.exchangerates.views.api import (
    ExChangeRateListAPIView,
    ExChangeRateDetailAPIView,
)

app_name = "exchangerate"

urlpatterns = [
    path("", ExChangeRateListAPIView.as_view(), name="index"),
    re_path(
        r"^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$",
        ExChangeRateDetailAPIView.as_view(),
        name="detail",
    ),
]
