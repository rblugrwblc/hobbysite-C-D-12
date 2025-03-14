# <appname>/urls.py
from django.urls import path
from .views import blog_article_list, blog_article_detail
urlpatterns = [
path('articles', blog_article_list, name='list_view'),
path('article/<int:article_id>', blog_article_detail, name='detail_view'),
]

app_name = "blog"
