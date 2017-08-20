from django import forms
from django.contrib.admin.widgets import AdminTextareaWidget
from django.core.files.storage import default_storage
from django.utils.safestring import mark_safe
from django.conf import settings


class BSMarkDownWidget(forms.Textarea):
    def __init__(self, attrs=None):
        super(BSMarkDownWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        """ Render widget.
        :returns: A rendered HTML
        """
        attrs.update({"data-provide": "markdown",
                      "data-iconlibrary": "fa",
                      "id": "editor",
                      })
        html = super(BSMarkDownWidget, self).render(name, value, attrs)
        # attrs = self.build_attrs(attrs)
        # html += editor_js_initialization("#%s" % attrs['id'])
        return mark_safe(html)

    class Media:
        css = {
            'screen': (settings.STATIC_URL + 'css/bootstrap-markdown.min.css',),
        }
        js = [
            settings.STATIC_URL + 'js/markdown.js',
            settings.STATIC_URL + 'js/bootstrap-markdown.js',
            settings.STATIC_URL + 'js/bootstrap-markdown.zh.js',
        ]
