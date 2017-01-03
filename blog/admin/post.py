from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_display    = ('title', 'status', 'created_date', 'last_update')
    list_filter     = ('status', )


