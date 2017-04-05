"""dugong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from views.home import HomeView

handler500 = 'views.errors.page_error'
handler404 = 'views.errors.not_found'


urlpatterns = staticfiles_urlpatterns()

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include( 'django_markdown.urls')),


    url(r'^blog/', include('blog.urls')),
    url(r'^project/', include('opensource.urls.web')),
    # url(r'^comments/', include('django_comments.urls')),

    # home page
    url(r'^$', HomeView.as_view(), name='homepage'),
]

# silk
urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]

from views.search import ProjectSearchView

urlpatterns += [
    # url(r'^search/', include('haystack.urls')),
    url(r'^search/autocomplete/?$', 'views.search.autocomplete', name='search-autocomplete'),
    url(r'^search/?$', ProjectSearchView.as_view(), name='project-search-view'),
]


'''
    api url config
'''
urlpatterns +=[
    url(r'^api/books/', include('books.urls')),
    url(r'^api/opensource/', include('opensource.urls.api')),
]


from blog.sitemaps import PostSitemap
sitemaps = {
    'blog': PostSitemap,
}

from django.contrib.sitemaps import views
from django.views.decorators.cache import cache_page
urlpatterns += [
    url(r'^sitemap\.xml$', cache_page(86400)(views.sitemap),
                            {'sitemaps': sitemaps},
                            name='post_sitemaps'),
]


from blog.feeds import PostFeeds
urlpatterns += [
    url(r'^feed/posts/$', PostFeeds(), name='blog-post-feed')
]


from django.contrib.flatpages import views
urlpatterns += [
    url(r'^pages/(?P<url>.*/?)$', views.flatpage),
]
