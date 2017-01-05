from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSitemap(Sitemap):

    changefreq = "never"
    priority = 1.0
    limit = 1000

    def items(self):
        return Post.objects.filter(status=Post.publish).\
            order_by('last_update')

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.last_update