from django.conf.urls import url
from ..views import IndexSearchView

urlpatterns = [
    url(r"^$", IndexSearchView.as_view(), name="index"),
]
