import logging
import re
try:
    from haystack.utils.highlighting import Highlighter
except ImportError:
    Warning("please install django-haystack")
# from django.utils.html import strip_tags

logger = logging.getLogger("django")


class TitleHighlighter(Highlighter):
    def render_html(self, highlight_locations=None, start_offset=None, end_offset=None):
        highlight_text = self.text_block
        # logger.info(highlight_text)

        # Prepare the highlight template
        if self.css_class:
            hl_start = '<%s class="%s">' % (self.html_tag, self.css_class)
        else:
            hl_start = "<%s>" % self.html_tag

        hl_end = "</%s>" % self.html_tag

        # ignore case
        def process_word(match_obj):
            logger.info(match_obj)
            if match_obj.group(0):
                match_word = match_obj.group(0)
                logger.info(match_word)
                return "{start}{word}{end}".format(
                    start=hl_start, word=match_word, end=hl_end
                )

        for word in self.query_words:
            pattern = re.compile(r"(%s)" % word, flags=re.IGNORECASE)
            logger.info(pattern)
            highlight_text = re.sub(pattern, process_word, highlight_text)
        return highlight_text
