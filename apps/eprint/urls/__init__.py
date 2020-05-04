from django.urls import path
from ..views import EprintListView, EprintDetailView, EprintKeyWordsView

urlpatterns = [
    path("", EprintListView.as_view(), name="index"),
    path("kw/", EprintKeyWordsView.as_view(), name="keywords"),
    path("<slug:slug>/", EprintDetailView.as_view(), name="detail"),
]

app_name = "eprint"
