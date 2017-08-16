from django.contrib import admin
from django_markdown.widgets import AdminMarkdownWidget
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'published_at']
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownWidget}
    }


