from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, home

app_name = "wiki"

urlpatterns = [
    path('', home, name='home'), 
    path("articles/", ArticleListView.as_view(), name="article_list"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
]