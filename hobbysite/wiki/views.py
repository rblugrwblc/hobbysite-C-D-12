from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm

def wiki_article_list(request):
    categories = ArticleCategory.objects.all()
    articles = Article.objects.all()
    return render(request, 'wiki_article_list.html', {'articles': articles,
                                                      'categories':categories})

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
    if request.method == 'POST':
        wiki_article_form = ArticleForm(request.POST)

        # Make sure user has a profile, if none redirect to list_view
        try: 
            user_profile = request.user.profile
        except: 
            return redirect(reverse('wiki:list_view'))
        
        if wiki_article_form.is_valid():
            form = wiki_article_form.save(commit=False)
            form.author = request.user.profile
            form.save()

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
        form = ArticleForm(instance = article)
    
    return render(request, 'wiki_article_form.html', {'form': form})


def home(request): 
    return HttpResponse("<h1>Welcome to the Wiki.</h1><p>Go to <a href='/wiki/articles/'>Articles</a></p>")
