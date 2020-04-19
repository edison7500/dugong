from django.urls import path
from ..views import EprintListView, EprintDetailView

urlpatterns = [
    path("", EprintListView.as_view(), name="index"),
    path("<slug:slug>/", EprintDetailView.as_view(), name="detail"),
]

app_name = "eprint"
