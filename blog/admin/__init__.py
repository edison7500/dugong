from django.contrib import admin
from post import PostAdmin
from blog.models import Post


admin.site.register(Post, PostAdmin)