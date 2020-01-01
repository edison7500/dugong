# from django.conf.urls import url
from django.urls import path

from apps.blog.views import BlogListView, BlogDetailView, PostTagListView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="index"),
    # url(r'^(?P<year>[0-9]{4})/$',
    #     BlogYearArchiveView.as_view(), name="year_archive"),
    path("tags/<int:tid>/", PostTagListView.as_view(), name="tags"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="detail"),
]
