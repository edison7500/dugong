from django.conf.urls import url
from opensource.views.api import PeopleListAPIView


urlpatterns = [
    url(r'^$', PeopleListAPIView.as_view(), name='list'),
]