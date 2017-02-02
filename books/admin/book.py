from django.contrib import admin
from books.models import Image
from books.admin.forms import BookAdminForm
from django.utils.translation import ugettext_lazy as _


def make_published(self, request, queryset):
    rows_updated = queryset.update(status=True)
    if rows_updated == 1:
        message_bit = "1 book was"
    else:
        message_bit = "%s books were" % rows_updated
    self.message_user(request, "%s successfully marked as published." % message_bit)
make_published.short_description = _('mark selected articles as published')



class BookImageInlineAdmin(admin.StackedInline):
    model = Image
    extra = 1


class BookAdmin(admin.ModelAdmin):
    form            = BookAdminForm
    list_display    = ['title', 'price', 'status', 'asin', 'create_datetime']
    search_fields   = ['title']
    list_filter     = ['status',]

    ordering        = ['-create_datetime']

    inlines         = [BookImageInlineAdmin,]
    actions         = [make_published, ]

    def get_image_tag(self, obj):

        return
