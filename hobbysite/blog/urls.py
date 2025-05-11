# <appname>/urls.py
from django.urls import path
from .views import article_list, article_detail, article_addimage, article_edit
urlpatterns = [
path('articles', article_list, name='article_list'),
path('article/<int:article_id>', article_detail, name='article_detail'),
path('article/add', article_addimage, name='article_addimage'),
path('article/<int:article_id>/edit', article_edit, name='article_edit'),
]

app_name = "blog"