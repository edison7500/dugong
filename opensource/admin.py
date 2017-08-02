from django.contrib import admin
from opensource.models import Project, Category, Author, PostProject

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'url')
    list_per_page = 30
    search_fields = ['author', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_per_page = 30


class ProjectAdmin(admin.ModelAdmin):
    list_display        = ('author', 'name', 'display', 'github_url',)
    list_display_links  = ('name', )
    search_fields       = ('author', 'name', )
    list_filter         = ('display', )
    fields              = (('author', 'name'), 'display', 'category', 'readme')
    list_per_page       = 30


class PostPorjectAdmin(admin.ModelAdmin):
    list_display = ('url', 'category')
    search_fields = ['url', ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(PostProject, PostPorjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
