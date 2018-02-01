from django.contrib import admin
from opensource.models import (Project, Category,
                               Organization,
                               People, PostProject)


# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'location', 'web_site',
                    'email', 'created_at')
    list_per_page = 30


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at')
    list_per_page = 30
    search_fields = ['author', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 30


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'category', 'display',
                    'github_url', 'created_at')
    list_display_links = ('name',)
    search_fields = ('author', 'name',)
    list_filter = ('display', 'category', )
    fields = (('author', 'name'), 'display', 'category', 'readme')
    list_per_page = 30


class PostProjectAdmin(admin.ModelAdmin):
    list_display = ('url', 'category', 'created_at')
    search_fields = ['url', ]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(PostProject, PostProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
