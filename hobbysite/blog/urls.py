# <appname>/urls.py
from django.urls import path
from .views import blog_article_list, blog_article_detail, article_addimage, article_edit
urlpatterns = [
path('articles', blog_article_list, name='list_view'),
path('article/<int:article_id>', blog_article_detail, name='detail_view'),
path('article/add', article_addimage, name='article_addimage'),
path('article/<int:article_id>/edit', article_edit, name='article_edit'),
]

app_name = "blog"
