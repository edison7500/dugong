from django.contrib import admin
# from django.contrib.flatpages.models import FlatPage

from .post import PostAdmin
from blog.models import Post

admin.site.register(Post, PostAdmin)
# admin.site.register(PostImage, PostImageAdmin)

# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)
