from django.contrib import admin
# from django.utils.translation import ugettext_lazy as _


class CategoryAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    list_display    = ('title', 'category', 'status', 'created_datetime', 'updated_datetime')
    list_filter     = ('status', )