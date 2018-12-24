from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Jiaxin API DOCs')

urlpatterns = [
    url(r'^opensource/', include('opensource.urls.api', namespace='opensource')),
    url(r'^tutorials/', include('tutorials.urls.api', namespace='tutorials')),
    url(r'^docs/$', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
