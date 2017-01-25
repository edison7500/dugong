from django.contrib import admin
from books.models import Image


class BookImageInlineAdmin(admin.StackedInline):
    model = Image
    extra = 1


class BookAdmin(admin.ModelAdmin):

    inlines = [BookImageInlineAdmin,]
