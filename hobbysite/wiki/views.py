from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Article, ArticleCategory

def wiki_article_list(request):
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    return render(request, 'wiki_article_list.html', {'articles': articles,
                                                      'categories':categories})

def wiki_article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'wiki_article_detail.html', {'article': article})

def home(request): 
    return HttpResponse("<h1>Welcome to the Wiki.</h1><p>Go to <a href='/wiki/articles/'>Articles</a></p>")
