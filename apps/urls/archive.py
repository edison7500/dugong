from django.conf.urls import url
from apps.blog.views import BlogYearArchiveView

app_name = "archive"

urlpatterns = [
    url('^blog/(?P<year>[0-9]{4})/?$',
        BlogYearArchiveView.as_view(), name='blog_year'),
]
