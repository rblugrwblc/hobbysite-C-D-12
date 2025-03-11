from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ProductType, Product

# Create your views here.
def item(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product.html', {'product':product})
    
def item_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})
