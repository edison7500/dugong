from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# from django_markdown.widgets import AdminMarkdownWidget
# from markdownx.admin import MarkdownxModelAdmin
# from markdownx.fields import MarkdownxFormField

# from blog.admin.forms import BlogAdminForm
from blog.models import PostImage


class PostImageInlineAdmin(admin.StackedInline):
    model = PostImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    # form = BlogAdminForm

    list_display = ('title', 'status', 'created_date', 'last_update')
    list_filter = ('status',)
    search_fields = ('title',)
    list_per_page = 30
    inlines = (PostImageInlineAdmin,)


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.admin import FlatPageAdmin
#
from django.db import models


# from redactor.widgets import RedactorEditor

# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    form = FlatpageForm
    # formfield_overrides = {
    # models.TextField: {'widget': MarkdownxFormField()}
    #     models.TextField: {'widget': RedactorEditor(
    #         redactor_options={
    #             'formatting': ['p', 'blockquote', 'h2', 'h3'],
    #             # 'buttons': ['formatting', 'bold', 'italic',
    #             #         'deleted', 'lists', 'link', 'unorderedlist', 'orderedlist',
    #             #         'alignment', 'horizontalrule', 'html'],
    #             'lang': 'zh_cn',
    #         },
    #         # attrs={}
    #     )},
    # }

    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                # 'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )
# Re-register FlatPageAdmin
