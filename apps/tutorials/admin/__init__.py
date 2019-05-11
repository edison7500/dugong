from django.contrib import admin
from apps.tutorials.admin.tutorial import TutorialAdmin
from apps.tutorials.models import Tutorial

admin.site.register(Tutorial, TutorialAdmin)
