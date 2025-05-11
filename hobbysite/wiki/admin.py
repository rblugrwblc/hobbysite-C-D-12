from django.contrib import admin
from .models import Article, ArticleCategory

# from .models import ArticleCategory, Article, Comment

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created_on', 'updated_on']
    list_filter = ['category']
    search_fields = ['title', 'entry']

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#    list_display = ['author', 'article', 'created_on']
#    search_fields = ['entry']
