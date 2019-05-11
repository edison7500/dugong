from django.contrib.sitemaps import Sitemap
from apps.blog.models import Post


class PostSitemap(Sitemap):

    changefreq = "never"
    priority = 1.0
    limit = 500

    def items(self):
        return Post.objects.filter(status=Post.publish).\
            order_by('-created_date')

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.created_date