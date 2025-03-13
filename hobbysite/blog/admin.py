from django.contrib import admin
from .models import Article, Article_Category

class Article_Admin(admin.ModelAdmin):
    model = Article

class Article_Category_Admin(admin.ModelAdmin):
    model = Article_Category


admin.site.register(Article_Admin)
admin.site.register(Article_Category_Admin)