from django.shortcuts import render, HttpResponse

def home(request): 
    return HttpResponse("project moment")