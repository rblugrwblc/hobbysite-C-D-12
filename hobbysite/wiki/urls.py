from django.urls import path, include
from .views import wiki_article_add, wiki_article_list, wiki_article_detail, home

app_name = "wiki"

urlpatterns = [
    path('', home, name='home'), 
    path('articles/', wiki_article_list, name='list_view'),
    path('articles/<int:pk>/', wiki_article_detail, name='detail_view'),
    path('articles/add', wiki_article_add, name ='article_view'),
]
