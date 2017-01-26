from django.contrib import admin
from books.models import Image
from books.admin.forms import BookAdminForm


class BookImageInlineAdmin(admin.StackedInline):
    model = Image
    extra = 1


class BookAdmin(admin.ModelAdmin):
    form            = BookAdminForm
    list_display    = ['title', 'price', 'asin', 'create_datetime']
    search_fields   = ['title']

    ordering        = ['-create_datetime']

    inlines         = [BookImageInlineAdmin,]

    def get_image_tag(self, obj):

        return
