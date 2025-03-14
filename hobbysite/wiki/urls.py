from django.urls import path, include
from .views import article_list, article_detail, home

app_name = "wiki"

urlpatterns = [
    path('', home, name='home'), 
    path('articles/', article_list, name='article_list'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
]