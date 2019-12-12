from django.conf.urls import url
from ..views import IndexSearchView

app_name = "serach"

urlpatterns = [
    url(r"^$", IndexSearchView.as_view(), name="index"),
]
