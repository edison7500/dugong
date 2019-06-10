from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from apps.images.models import Image

# from blog.models import PostImage


class PostImageInlineAdmin(GenericStackedInline):
    model = Image
    fields = ["file", "description"]
    extra = 1


class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "status", "tag_string", "created_date", "last_update")
    list_filter = ("status",)
    search_fields = ("title",)
    list_per_page = 30
    inlines = (PostImageInlineAdmin,)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")


# class PostImageAdmin(admin.ModelAdmin):
#     list_display = ('image',)

#
# from django.contrib.flatpages.forms import FlatpageForm
# from django.contrib.flatpages.admin import FlatPageAdmin
#
#
# # Define a new FlatPageAdmin
# class FlatPageAdmin(FlatPageAdmin):
#     form = FlatpageForm
#     # formfield_overrides = {
#     # models.TextField: {'widget': MarkdownxFormField()}
#     #     models.TextField: {'widget': RedactorEditor(
#     #         redactor_options={
#     #             'formatting': ['p', 'blockquote', 'h2', 'h3'],
#     #             # 'buttons': ['formatting', 'bold', 'italic',
#     #             #         'deleted', 'lists', 'link', 'unorderedlist', 'orderedlist',
#     #             #         'alignment', 'horizontalrule', 'html'],
#     #             'lang': 'zh_cn',
#     #         },
#     #         # attrs={}
#     #     )},
#     # }
#
#     fieldsets = (
#         (None, {'fields': ('url', 'title', 'content', 'sites')}),
#         (_('Advanced options'), {
#             'classes': ('collapse',),
#             'fields': (
#                 # 'enable_comments',
#                 'registration_required',
#                 'template_name',
#             ),
#         }),
#     )
# Re-register FlatPageAdmin
