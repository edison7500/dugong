from django.urls import path
from ..views import EprintListView

urlpatterns = [
    path("", EprintListView.as_view(), name="index")
]

app_name = "eprint"
