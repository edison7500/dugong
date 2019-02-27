from django.conf.urls import url

from apps.tutorials.views.web import (
    TutorialListView,
    TutorialDetailView
)

urlpatterns = [
    url(r'^$', TutorialListView.as_view(), name='list'),
    url(r'^(?P<slug>\d+)\.htm$', TutorialDetailView.as_view(), name='detail'),
    # url(r'^create\.htm$', TutorialCreateView.as_view(), name='create'),
    # url(r'^(?P<slug>\d+)/update\.htm$', TutorialUpdateView.as_view(), name='update'),
]
