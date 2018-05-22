from django.contrib import admin
from tutorials.admin.tutorial import TutorialAdmin
from tutorials.models import Tutorial

admin.site.register(Tutorial, TutorialAdmin)
