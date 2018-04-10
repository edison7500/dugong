from django.conf.urls import url
from tutorials.views.api import TutorialsListView


urlpatterns = [
    url(r'^$', TutorialsListView.as_view(), name='list'),
]