from django.conf.urls import url, include
from blog.views import BlogListView, BlogDetailView, PostTagListView


urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='list'),
    url(r'^tags/(?P<tag_id>\d+/?$)', PostTagListView.as_view(), name='tags'),
    url(r'^(?P<slug>[\w|\-]+)/?$', BlogDetailView.as_view(), name='detail'),
]