from django.conf.urls import url
from tutorials.views.web import TutorialListView, TutorialDetailView


urlpatterns = [
    url(r'^$', TutorialListView.as_view(), name='list'),
    url(r'^(?P<slug>\d+)\.htm$', TutorialDetailView.as_view(), name='detail'),
]