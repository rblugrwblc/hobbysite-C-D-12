# appname/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Article_Category

def article_list(request):
    categories = Article_Category.objects.all()
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles':articles, 
                                                 'categories':categories} )

def article_detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'article_detail.html', {'article':article} )