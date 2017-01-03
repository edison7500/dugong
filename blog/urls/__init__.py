from django.conf.urls import url, include
from blog.views import BlogListView, BlogDetailView


urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='web_blog_list'),
    url(r'^(?P<slug>[\w|\-]+)/?', BlogDetailView.as_view(), name='web_blog_detail'),
]