from django.contrib import admin

from .post import PostAdmin
from apps.blog.models import Post

admin.site.register(Post, PostAdmin)
