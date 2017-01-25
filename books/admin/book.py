from django.contrib import admin
from books.models import Image
from books.admin.forms import BookAdminForm


class BookImageInlineAdmin(admin.StackedInline):
    model = Image
    extra = 1


class BookAdmin(admin.ModelAdmin):
    form            = BookAdminForm
    search_fields   = ['title']

    inlines         = [BookImageInlineAdmin,]
