# appname/views.py
from django.http import HttpResponse

def article_home(request):
    return HttpResponse('This is the Blog Home Page')

def article_detail(request):
    return HttpResponse('This is the Articles DEtailed View')