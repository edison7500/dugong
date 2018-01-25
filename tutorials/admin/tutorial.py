# coding=utf-8
from django.contrib import admin
# from django_markdown.widgets import AdminMarkdownWidget
from django.db import models
from tutorials.models import TutorialImage


# from tutorials.forms.widgets import BSMarkDownWidget

class TutorialImageInlineAdmin(admin.StackedInline):
    model = TutorialImage
    fields = ['image', 'is_cover']
    extra = 1


class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'tags', 'status', 'published_at']
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminMarkdownWidget}
    # }
    inlines = [TutorialImageInlineAdmin, ]
