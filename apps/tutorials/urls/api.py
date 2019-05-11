from django.conf.urls import url
from apps.tutorials.views.api import (
    TutorialsListView,
    TutorialsDetailView
)


urlpatterns = [
    url(r'^$', TutorialsListView.as_view(), name='list'),
    url(r'^(?P<slug>\d+)/?$', TutorialsDetailView.as_view(), name='detail'),
]