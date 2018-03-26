from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='JiaXin API', public=False)

urlpatterns = [
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^opensource/', include('opensource.urls.api', namespace='opensource')),
    url(r'^schema/$', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
