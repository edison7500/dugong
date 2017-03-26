from django.conf.urls import url
from opensource.views.web import ProjectDetailView


urlpatterns =[
    url(r'^(P<slug>[\w\/]+)', ProjectDetailView.as_view(), name='web-project-detail')
]