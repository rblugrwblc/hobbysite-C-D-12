# <appname>/urls.py
from django.urls import path
from .views import article_list, article_detail
urlpatterns = [
path('articles', article_list, name='article_list'),
path('article/<int:article_id>', article_detail, name='article_detail'),
]
# This might be needed, depending on your Django version
app_name = "blog"