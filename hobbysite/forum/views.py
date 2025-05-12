from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import ThreadCategory, Thread
from .forms import ThreadForm, CommentForm
from django.utils.timezone import now

def thread_list(request):
    categories = ThreadCategory.objects.prefetch_related('threads').all()
    user_threads = []
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        user_profile = request.user.profile
        user_threads = Thread.objects.filter(author=user_profile)
        for category in categories:
            category.filtered_threads = category.threads.exclude(author=user_profile)
    else:
        for category in categories:
            category.filtered_threads = category.threads.all()

    return render(request, 'thread_list.html', {'categories': categories, 'user_threads': user_threads})

def thread_detail(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    comments = thread.comments.all()
    related_threads = Thread.objects.filter(category=thread.category).exclude(id=thread.id)[:2]

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.thread = thread
            comment.author = request.user.profile
            comment.save()
            return redirect(thread.get_absolute_url())
    else:
        comment_form = CommentForm()

    return render(request, 'thread_details.html', {
        'thread': thread,
        'comments': comments,
        'related_threads': related_threads,
        'comment_form': comment_form
    })


@login_required
def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user.profile
            thread.save()
            return redirect(thread.get_absolute_url())
    else:
        form = ThreadForm()
        form.fields['author_field'].initial = str(request.user.profile)
        form.fields['created_on_field'].initial = now()
        form.fields['updated_on_field'].initial = now()

    return render(request, 'thread_create.html', {'form': form})

@login_required
def thread_edit(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    if thread.author != request.user.profile:
        return redirect('forum:list_view')

    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES, instance=thread)
        if form.is_valid():
            form.save()
            return redirect(thread.get_absolute_url())
    else:
        form = ThreadForm(instance=thread)
        form.fields['author_field'].initial = str(thread.author)
        form.fields['created_on_field'].initial = thread.created_on
        form.fields['updated_on_field'].initial = thread.updated_on

    return render(request, 'thread_edit.html', {'form': form})



