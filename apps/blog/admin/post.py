# from ajax_select import register, LookupChannel
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from apps.images.models import Image


# @register("tags")
# class TagsLookup(LookupChannel):
#     model = Tag
#
#     def get_query(self, q, request):
#         return self.model.objects.filter(name=q)
#
#     def format_item_display(self, item):
#         return "<span class='tag'>%s</span>" % item.name


class PostImageInlineAdmin(GenericStackedInline):
    model = Image
    fields = ["file", "description"]
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "tag_string",
        "created_at",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = ("title",)
    list_per_page = 30
    inlines = (PostImageInlineAdmin,)
    # form = PostForm

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")
