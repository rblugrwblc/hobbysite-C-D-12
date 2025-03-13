# appname/views.py
from django.http import HttpResponse
from django.shortcuts import render

def article_home(request):
    ctx = {
        "tasks": [
        "task 1",
        "task 2",
        "task 3",
        "task 4"
        ]
    }
    return render(request, 'article_home.html', ctx)

def article_detail(request):
    return HttpResponse('This is the Articles DEtailed View')