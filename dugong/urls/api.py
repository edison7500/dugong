from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Jiaxin API DOCs')

urlpatterns = [
    url(r'^docs/$', schema_view),
    url(r'^tutorials/', include('apps.tutorials.urls.api', namespace='tutorials')),
    url(r'^opensource/', include('opensource.urls.api', namespace='opensource')),
    url(r'^books/', include('apps.books.urls.api', namespace='book')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
