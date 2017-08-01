from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from opensource.views.api import (  OpenSourceListAPIView,
                                    OpenSourceDetailAPIView,
                                    OpenSourceStatusListView,
                                    PostProjectListAPIView
                                    )
# from rest_framework.urlpatter


urlpatterns =[
    url(r'^$', OpenSourceListAPIView.as_view(), name='open-source-api-list'),
    url(r'^fetch/project/?$', PostProjectListAPIView.as_view(), name='post-project-api-list'),
    url(r'^(?P<pid>\d+)/stats/?$', OpenSourceStatusListView.as_view(), name='open-source-status-api-list'),
    url(r'^(?P<identified_code>\w+)/?$', OpenSourceDetailAPIView.as_view(), name='open-source-api-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])