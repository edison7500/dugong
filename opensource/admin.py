from django.contrib import admin
from opensource.models import Project, Category, Status, PostProject

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ProjectAdmin(admin.ModelAdmin):
    list_display    = ('author', 'name', 'desc', 'github_url')
    search_fields   = ('author', 'name', )
    list_filter     = ('display', )


class PostPorjectAdmin(admin.ModelAdmin):
    list_display    = ('url', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(PostProject, PostPorjectAdmin)