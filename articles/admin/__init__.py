from django.contrib import admin
from articles.models import Article, Category
from articles.admin.article import ArticleAdmin, CategoryAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)