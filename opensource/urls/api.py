from django.conf.urls import url
from opensource.views.api import OpenSourceListAPIView


urlpatterns =[
    url(r'^$', OpenSourceListAPIView.as_view(), name='open-source-api-list'),
]