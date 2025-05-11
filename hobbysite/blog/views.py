# appname/views.py
from django.shortcuts import render
from .models import Article, ArticleCategory

def article_list(request):
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles':articles, 
                                                 'categories':categories} )

def article_detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'article_detail.html', {'article':article} )

def article_edit(request, article_id):
    
    return render(request, 'article_edit.html')

def article_addimage(request):
  
    return render(request, 'article_addimage.html')