# appname/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, ArticleCategory

def blog_article_list(request):
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    return render(request, 'blog_article_list.html', {'articles':articles, 
                                                 'categories':categories} )

def blog_article_detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'blog_article_detail.html', {'article':article} )
