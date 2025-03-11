from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import PostCategory, Post


def PostListView(request):
    categories = PostCategory.objects.all()
    return render(request, 'post_list.html', {'categories': categories} )


def PostDetailedView(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Post does not exist.")
    
    return render(request, 'post_details.html', {'post': post})

