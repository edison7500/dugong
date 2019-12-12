# from ajax_select import urls as ajax_select_urls
from django.conf import settings
# from django.conf.urls import include, url
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from controlcenter.views import controlcenter
from apps.blog.views import BlogListView

# handler500 = "apps.main.views.errors.page_error"
# handler404 = "apps.main.views.errors.not_found"

urlpatterns = [
    path("admin/", admin.site.urls),
    # re_path(r'^admin/dashboard/', controlcenter.urls),
    # url(r'^ajax_select/', include(ajax_select_urls)),
    # url(r"^comments/", include("django_comments.urls", namespace="comments")),
    path("blog/", include("apps.blog.urls", namespace="blog")),
    re_path(r"^tutorials/", include("apps.tutorials.urls", namespace="tutorials")),
    re_path(r"^o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]

urlpatterns += [path("images/", include("apps.images.urls", namespace="images"))]

urlpatterns += [path("archive/", include("apps.urls.archive", namespace="archive",))]

#
# django allauth url config
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns += [re_path(r"^account/", include("allauth.urls"))]

#
# search url config
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns += [re_path(r"^search/", include("apps.search.urls.search", namespace="search"))]

#
# api url config
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns += [path("api/", include("dugong.urls.api", namespace="api"))]

urlpatterns += [re_path(r"^$", BlogListView.as_view(), name="homepage")]

#
# site map config
#
from apps.blog.sitemaps import PostSitemap

sitemaps = {"blog": PostSitemap}

from django.contrib.sitemaps import views
from django.views.decorators.cache import cache_page

urlpatterns += [
    re_path(
        r"^sitemap\.xml$",
        cache_page(86400)(views.sitemap),
        {"sitemaps": sitemaps},
        name="post_sitemaps",
    )
]

from apps.blog.feeds import PostFeeds

urlpatterns += [re_path(r"^feed/posts/$", PostFeeds(), name="blog-post-feed")]

from django.contrib.flatpages import views

urlpatterns += [re_path(r"^pages/(?P<url>.*/?)$", views.flatpage)]

urlpatterns += staticfiles_urlpatterns()

#
# debug url config
# ----------------------------------------------------------------------------------------------------------------------
# if settings.DEBUG:
#     if "debug_toolbar" in settings.INSTALLED_APPS:
#         import debug_toolbar
#         urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

admin.site.site_header = "jiaxin.im"
admin.site.site_title = "jiaxin.im"
admin.site.index_title = "Welcome to JIAXIN.IM"
