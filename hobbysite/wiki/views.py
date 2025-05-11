from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm
from user_management.models import Profile

def wiki_article_list(request):
    categories = ArticleCategory.objects.all().prefetch_related('article_set')
    
    articles = Article.objects.all()
    user_articles = []
    
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            user_articles = articles.filter(author=user_profile)
            articles = articles.exclude(author=user_profile) 
        except Profile.DoesNotExist:
            pass

    articles_by_category = {
        category: articles.filter(category=category) 
        for category in categories
    }

    return render(request, 'wiki_article_list.html', {
        'articles_by_category': articles_by_category,
        'categories': categories,
        'user_articles': user_articles
    })

def wiki_article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    related_articles = Article.objects.filter(category=article.category).exclude(pk=article.pk)[:2]

    comments = article.comments.all()
    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid() and request.user.is_authenticated:
        comment = comment_form.save(commit=False)
        comment.author = request.user.profile
        comment.article = article
        comment.save()
        return redirect('wiki:detail_view', pk=article.pk)

    return render(request, 'wiki_article_detail.html', {
        'article': article,
        'related_articles': related_articles,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
def wiki_article_add(request):
    try: 
        user_profile = request.user.profile
    except: 
        return redirect(reverse('wiki:list_view'))

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid(): 
            article = form.save(commit=False)
            article.author = user_profile
            article.save()
            return redirect(reverse('wiki:list_view'))
    else:
        form = ArticleForm()

    return render(request, 'wiki_article_form.html', {'form': form})

@login_required 
def wiki_article_edit(request, pk): 
    article = get_object_or_404(Article, pk=pk)

    # Check if user profile exists and then if they are author
    try:
        user_profile = request.user.profile
    except:
        return redirect(reverse('wiki:list_view')) 

    if article.author != request.user.profile: 
        return redirect(reverse('wiki:list_view'))
    
    if request.method == 'POST': 
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            form.save()
            return redirect(reverse('wiki:list_view'))
    else:
        form = ArticleForm(instance=article)
 
    return render(request, 'wiki_article_form.html', {'form': form})


def home(request): 
    return HttpResponse("<h1>Welcome to the Wiki.</h1><p>Go to <a href='/wiki/articles/'>Articles</a></p>")
