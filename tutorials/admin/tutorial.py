from django.contrib import admin
from django_markdown.widgets import AdminMarkdownWidget
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownWidget}
    }


