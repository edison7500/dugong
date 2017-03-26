from django.conf.urls import url
from opensource.views.api import OpenSourceListAPIView, OpenSourceDetailAPIView


urlpatterns =[
    url(r'^$', OpenSourceListAPIView.as_view(), name='open-source-api-list'),
    url(r'^(?P<identified_code>\w+)/?$', OpenSourceDetailAPIView.as_view(), name='open-source-api-detail'),
]