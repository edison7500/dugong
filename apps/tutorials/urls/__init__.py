from django.conf.urls import url

from apps.tutorials.views.web import (
    TutorialListView,
    TutorialDetailView
)

app_name = "tutorials"

urlpatterns = [
    url(r'^$', TutorialListView.as_view(), name='list'),
    url(r'^(?P<slug>\d+)\.htm$', TutorialDetailView.as_view(), name='detail'),
]
