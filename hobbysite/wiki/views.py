from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    templateName = "wiki/article_list.html"
    contextObjectName = "articles"

class ArticleDetailView(DetailView):
    model = Article
    templateName = "wiki/article_detail.html"
    contextObjectName = "article"

def home(request): 
    return HttpResponse("<h1>Welcome to the Wiki. </h1><p>Go to <a href='/wiki/articles/'>Articles</a></p>")
