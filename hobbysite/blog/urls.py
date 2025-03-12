# <appname>/urls.py
from django.urls import path
from .views import article_home, article_detail
urlpatterns = [
path('articles', article_home, name='article_home'),
path('article/1', article_detail, name='article_detail'),
]
# This might be needed, depending on your Django version
app_name = "blog"