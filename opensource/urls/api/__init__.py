from django.conf.urls import url, include

from opensource.views.api import (
                                    OpenSourceListAPIView,
                                    OpenSourceDetailAPIView,
                                    OpenSourceStatusListView,
                                    PostProjectListAPIView
                                    )


urlpatterns = [
    url(r'^$', OpenSourceListAPIView.as_view(), name='list'),

    url(r'^fetch/project/?$', PostProjectListAPIView.as_view(), name='post-project-api-list'),
    url(r'^(?P<pid>\d+)/stats/?$', OpenSourceStatusListView.as_view(), name='stats'),
]


urlpatterns += [
    url(r'^organization/', include('opensource.urls.api.organization', namespace='organization')),
    url(r'^author/', include('opensource.urls.api.author', namespace='author')),
]


urlpatterns += [
    url(r'^(?P<identified_code>\w+)/?$', OpenSourceDetailAPIView.as_view(), name='detail'),
]
