# coding=utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views.home import HomeView

handler500 = 'views.errors.page_error'
handler404 = 'views.errors.not_found'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls', namespace='comments')),

    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^project/', include('opensource.urls.web')),
    url(r'^tutorials/', include('tutorials.urls', namespace='tutorials')),
    url(r'^accounts/', include('allauth.urls')),

    url('^markdown/', include('django_markdown.urls')),
    # home page
    url(r'^$', HomeView.as_view(), name='homepage'),
]

from views.search import ProjectSearchView, autocomplete

urlpatterns += [
    url(r'^search/autocomplete/?$', autocomplete, name='search-autocomplete'),
    url(r'^search/?$', ProjectSearchView.as_view(), name='project-search-view'),
]

'''
    api url config
'''
urlpatterns += [
    url(r'^api/', include('dugong.urls.api', namespace='api')),

    # url(r'^docs/', include_docs_urls(title='JiaXinAPI Docs',
    #                                  public=False,
    #                                  permission_classes=[
    #                                      permissions.IsAdminUser,
    #                                  ])
    #     ),
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

urlpatterns += staticfiles_urlpatterns()

admin.site.site_header = "jiaxin.im"
admin.site.site_title = "jiaxin.im"
admin.site.index_title = "Welcome to JIAXIN.IM"

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
