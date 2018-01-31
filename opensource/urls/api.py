from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns

from opensource.views.api import (  AuthorListView,
                                    OpenSourceListAPIView,
                                    OpenSourceDetailAPIView,
                                    OpenSourceStatusListView,
                                    PostProjectListAPIView
                                    )


urlpatterns =[
    url(r'^$', OpenSourceListAPIView.as_view(), name='list'),
    url(r'^author/?$', AuthorListView.as_view(), name='author'),
    url(r'^fetch/project/?$', PostProjectListAPIView.as_view(), name='post-project-api-list'),
    url(r'^(?P<pid>\d+)/stats/?$', OpenSourceStatusListView.as_view(), name='stats'),
    url(r'^(?P<identified_code>\w+)/?$', OpenSourceDetailAPIView.as_view(), name='detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])