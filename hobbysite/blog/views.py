# appname/views.py
from django.shortcuts import render,redirect
from .models import Article, ArticleCategory
from .forms import CommentForm
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
    common_author_articles = Article.objects.filter(author = article.author).exclude(id=article_id)
    comments = article.comments.all()
    comment_form = None
    is_owner = False

    if request.user.is_authenticated and hasattr(request.user, 'profile') and article.author == request.user.profile:
        is_owner = True;
    

    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile
            comment.save()
            return redirect(article.get_absolute_url())
        
    else:
        comment_form = CommentForm()

    return render(request, 'blog_article_detail.html', {'article':article,
                                                        'common_articles':common_author_articles,
                                                        'comments':comments,
                                                        'form': comment_form,
                                                        'owner': is_owner} )

def blog_article_edit(request, article_id):
    
    return render(request, 'blog_article_edit.html')

def blog_article_create(request):
  
    return render(request, 'blog_article_create.html')
