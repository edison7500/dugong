from django.conf.urls import url
from opensource.views.api import OrganizationListAPIView, OrganizationDetailAPIView

urlpatterns = [
    # url(r''),
    url(r'^\/?$', OrganizationListAPIView.as_view(), name='list'),
    url(r'^\/(?P<name>\d+)/?$', OrganizationDetailAPIView.as_view(), name='detail'),
]