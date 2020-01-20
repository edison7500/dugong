# from ajax_select import register, LookupChannel
from django.contrib import admin
from taggit.models import Tag

# from apps.books.forms import BookForm
from apps.books.models import Book


# @register("tags")
# class TagsLookup(LookupChannel):
#     model = Tag
#
#     def get_query(self, q, request):
#         return self.model.objects.filter(name=q)
#
#     def format_item_display(self, item):
#         return u"<span class='tag'>%s</span>" % item.name


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "identified",
        "title",
        "author",
        "download_link",
        "tag_string",
        "updated_at",
        "created_at",
    ]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_per_page = 30

    # form = BookForm

    # def get_queryset(self, request):
    #     return super().get_queryset(request).prefetch_related('tags')


admin.site.register(Book, BookAdmin)
