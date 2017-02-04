#coding=utf-8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
# from django.utils.feedgenerator import Atom1Feed
from django.utils.encoding import smart_str
from django.utils.html import strip_tags, escape
from django.utils.translation import gettext_lazy as _
from django.utils.feedgenerator import Rss201rev2Feed

from blog.models import Post


from xml.sax.saxutils import XMLGenerator

class SimplerXMLGenerator(XMLGenerator):
    def addQuickElement(self, name, contents=None, attrs=None, escape=False):
        "Convenience method for adding an element with no children"
        if attrs is None: attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            if escape:
                self.characters(contents)
            else:
                if not isinstance(contents, unicode):
                    contents = unicode(contents, self._encoding)
                self._write(contents)
        self.endElement(name)


class PostsFeedGenerator(Rss201rev2Feed):

    mime_type = 'application/xml; charset=utf-8'
    def write(self, outfile, encoding):
        handler = SimplerXMLGenerator(outfile, encoding)
        handler.startDocument()
        handler.startElement("rss", self.rss_attributes())
        handler.startElement("channel", self.root_attributes())
        self.add_root_elements(handler)
        self.write_items(handler)
        self.endChannelElement(handler)
        handler.endElement("rss")


    def rss_attributes(self):
        attrs = super(PostsFeedGenerator, self).rss_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        attrs['xmlns:media'] = 'http://search.yahoo.com/mrss/'
        attrs['xmlns:georss'] = 'http://www.georss.org/georss'
        attrs['xmlns:dc'] ="http://purl.org/dc/elements/1.1/"
        return attrs

    def add_item_elements(self, handler, item):
        super(PostsFeedGenerator, self).add_item_elements(handler, item)

        if item['content_encoded'] is not None:
            handler.addQuickElement(u'content:encoded', item['content_encoded'], escape=False)


class PostFeeds(Feed):
    feed_type = PostsFeedGenerator
    title = u'图文频道>>果库|精英消费者南'
    link = "/blog/"
    author_email = "edison7500@gmail.com"
    feed_copyright = "since 2008 jiaxin.im All rights reserved."
    description = '技术宅的天下，python，django，scrapy，ios'

    # description_template = "web/feeds/article_description.html"

    # def get_object(self, request, *args, **kwargs):
    #     return getattr(get_object_or_404)

    def items(self):
        return Post.objects.filter(status=Post.publish)[:10]
        # return Article.objects.published().order_by('-pub_time')[0:20]

    def item_title(self, item):
        return escape(item.title)

    def item_link(self, item):
        return reverse('web_blog_detail', args=[item.slug])

    def item_author_name(self, item):
        return "http://jiaxin.im/"

    def item_pubdate(self, item):
        return item.last_update

    def item_description(self, item):
        content = strip_tags(item.content)
        # content = strip_tags(item.article.bleached_content)
        desc = content.split(u'。')
        # return "<![CDATA[%s]]>" % (desc[0] + u'。')
        return escape(desc[0] + u'。')

    def item_extra_kwargs(self, item):
        extra = {
                'content_encoded': ("<![CDATA[%s]]>" % smart_str(item.content)),
                }
        return extra