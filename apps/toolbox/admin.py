"""Admin for `toolbox` app."""

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import ToolBox
from .models import Category


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    list_display = ["slug", "title"]
    search_fields = ["title"]
    mptt_level_indent = 20


class ToolBoxAdmin(admin.ModelAdmin):
    # class Meta:
    list_display = ["slug", "logo_thumb", "category", "title", "created_at"]
    list_filter = ["category"]
    search_fields = ["title"]
    list_per_page = 50

    readonly_fields = ["slug", "logo_thumb"]


admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(ToolBox, ToolBoxAdmin)
