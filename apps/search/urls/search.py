from django.urls import path
from ..views import IndexSearchView

app_name = "search"

urlpatterns = [path("", IndexSearchView.as_view(), name="index")]
