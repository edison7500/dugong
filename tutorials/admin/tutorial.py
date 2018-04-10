# coding=utf-8
from django.contrib import admin
from tutorials.models import TutorialImage


class TutorialImageInlineAdmin(admin.StackedInline):
    model = TutorialImage
    fields = ['image', 'is_cover']
    extra = 1


class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags', 'status', 'published_at']
    inlines = [TutorialImageInlineAdmin, ]
