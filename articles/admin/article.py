from django.contrib import admin
from articles.models import Cover
# from django.utils.translation import ugettext_lazy as _


class CategoryAdmin(admin.ModelAdmin):
    pass


class CoverInlineAdmin(admin.StackedInline):
    model = Cover
    fields      = ['image',]
    extra       = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display    = ('title', 'category', 'status', 'created_datetime', 'updated_datetime')
    list_filter     = ('status', )

    ordering        = ['-created_datetime']

    inlines         = (CoverInlineAdmin,)