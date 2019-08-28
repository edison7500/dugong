from django.conf.urls import url
from ..views import SearchIndexView

urlpatterns = [
    url(r"^$", SearchIndexView.as_view(), name="index"),
]
