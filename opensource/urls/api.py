from django.conf.urls import url

from opensource.views.api import (  OrganizationListAPIView,
                                    AuthorListAPIView,
                                    OpenSourceListAPIView,
                                    OpenSourceDetailAPIView,
                                    OpenSourceStatusListView,
                                    PostProjectListAPIView
                                    )


urlpatterns =[
    url(r'^$', OpenSourceListAPIView.as_view(), name='list'),
    url(r'^author/?$', AuthorListAPIView.as_view(), name='author'),
    url(r'^organization/?$', OrganizationListAPIView.as_view(), name='organization'),
    url(r'^fetch/project/?$', PostProjectListAPIView.as_view(), name='post-project-api-list'),
    url(r'^(?P<pid>\d+)/stats/?$', OpenSourceStatusListView.as_view(), name='stats'),
    url(r'^(?P<identified_code>\w+)/?$', OpenSourceDetailAPIView.as_view(), name='detail'),
]

