from django.conf.urls import url, include
from blog.views import BlogListView, BlogDetailView, PostTagListView


urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='web_blog_list'),
    url(r'^tags/(?P<tag_id>\d+/?$)', PostTagListView.as_view(), name='web_blog_tags'),

    url(r'^(?P<slug>[\w|\-]+)/?$', BlogDetailView.as_view(), name='web_blog_detail'),
]