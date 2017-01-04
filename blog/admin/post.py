from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from blog.admin.forms import BlogAdminForm


class PostAdmin(admin.ModelAdmin):
    form = BlogAdminForm

    list_display    = ('title', 'status', 'created_date', 'last_update')
    list_filter     = ('status', )



from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from redactor.widgets import RedactorEditor

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    form = FlatpageForm
    formfield_overrides = {
        models.TextField: {'widget': RedactorEditor(
            redactor_options={
                'formatting': ['p', 'blockquote', 'h2', 'h3'],
                'buttons': ['formatting', 'bold', 'italic',
                        'deleted', 'lists', 'link', 'unorderedlist', 'orderedlist',
                        'alignment', 'horizontalrule', 'html'],
                'lang': 'zh_cn',
            },
            # attrs={}
        )},
    }


    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                # 'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )
# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)