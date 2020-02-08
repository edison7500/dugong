from django.urls import path
from apps.tutorials.views.api import TutorialsListView, TutorialsDetailView

app_name = "tutorials"

urlpatterns = [
    path("", TutorialsListView.as_view(), name="list"),
    path("<slug:slug>/", TutorialsDetailView.as_view(), name="detail"),
]
