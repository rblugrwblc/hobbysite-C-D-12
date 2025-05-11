# appname/views.py
from django.shortcuts import render
from .models import Article, ArticleCategory, Profile
from django.contrib.auth.decorators import login_required

@login_required
def blog_article_list(request):
    

    user_profile = request.user.profile
    categories = ArticleCategory.objects.all()
    articles_author = Article.objects.filter(author = user_profile)
    articles = Article.objects.exclude(author = user_profile)

    return render(request, 'blog_article_list.html', {'articles_author':articles_author,
                                                 'articles': articles, 
                                                 'categories':categories} )

def blog_article_detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'blog_article_detail.html', {'article':article} )

def blog_article_edit(request, article_id):
    
    return render(request, 'blog_article_edit.html')

def blog_article_create(request):
  
    return render(request, 'blog_article_create.html')
