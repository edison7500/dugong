from django.urls import path
from apps.exchangerates.views import ExChangeRateListView

app_name = "exchangerates"

urlpatterns = [path("", ExChangeRateListView.as_view(), name="index")]
