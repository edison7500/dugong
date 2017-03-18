from django.contrib import admin
from opensource.models import Project, Category, Status

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ProjectAdmin(admin.ModelAdmin):

    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
