# <appname>/urls.py
from django.urls import path
from .views import blog_article_list, blog_article_detail, blog_article_addimage, blog_article_edit
urlpatterns = [
path('articles', blog_article_list, name='list_view'),
path('article/<int:article_id>', blog_article_detail, name='detail_view'),
path('article/add', blog_article_addimage, name='article_addimage'),
path('article/<int:article_id>/edit', blog_article_edit, name='article_edit'),
]

app_name = "blog"
