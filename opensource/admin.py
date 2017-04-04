from django.contrib import admin
from opensource.models import Project, Category, Status, PostProject

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ProjectAdmin(admin.ModelAdmin):
    list_display        = ('author', 'name', 'display', 'github_url',)
    list_display_links  = ('name', )
    search_fields       = ('author', 'name', )
    list_filter         = ('display', )
    fields              = (('author', 'name'), 'display', 'category', 'readme')
    list_per_page       = 30


class PostPorjectAdmin(admin.ModelAdmin):
    list_display    = ('url', 'category')


admin.site.register(PostProject, PostPorjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
