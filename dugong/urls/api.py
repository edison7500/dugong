from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from apps.users.views.api import UserDetailsView

schema_view = get_swagger_view(title='Jiaxin API DOCs')

urlpatterns = [
    url(r'^docs/$', schema_view),
    url(r'^tutorials/', include('apps.tutorials.urls.api', namespace='tutorials')),
    url(r'^opensource/', include('opensource.urls.api', namespace='opensource')),
    url(r'^books/', include('apps.books.urls.api', namespace='book')),
]


urlpatterns += [
    url(r"^auth/", include('rest_auth.urls')),
    url(r"^rest/profile/?$", UserDetailsView.as_view(), name='oauth_user_profile'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
