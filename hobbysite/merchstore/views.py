from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Profile, ProductType, Product, Transaction
from .forms import ProductForm, TransactionForm

def item(request, id):
    
    product = Product.objects.get(pk=id)
    transaction_form = TransactionForm()
    user = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        transaction_form = TransactionForm(request.POST)

        if transaction_form.is_valid():
            amount = transaction_form.cleaned_data.get('amount')
            
            if amount <= product.stock:
                transaction = Transaction()
                transaction.buyer = user
                transaction.product = product
                transaction.amount = amount
                transaction.status = 'On cart'
                transaction.save()

                product.stock -= amount
                product.save()

                return redirect('merchstore:cart_view')

    
    return render(request, 'product.html', {'product':product,
                                            'form':transaction_form,})
    
def item_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

@login_required
def item_add(request):
    
    product_form = ProductForm()
    owner = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product = Product()
            product.name = product_form.cleaned_data.get('name')
            product.product_type = product_form.cleaned_data.get('product_type')
            product.owner = owner
            product.description = product_form.cleaned_data.get('description')
            product.price = product_form.cleaned_data.get('price')
            product.stock = product_form.cleaned_data.get('stock')
            product.status = product_form.cleaned_data.get('status')
            product.save()

            return redirect('merchstore:detail_view', product.id)
    
    return render(request, 'product_add.html', {'form': product_form,
                                                'owner': owner})

@login_required
def item_edit(request, id):
    
    product = Product.objects.get(pk=id)
    user = Profile.objects.get(user=request.user)

    if user != product.owner:
        return redirect('merchstore:detail_view', product.id)

    product_form = ProductForm(request.POST or None, instance=product)
    
    if request.method == 'POST' and product_form.is_valid():
        product_form.save()
        return redirect('merchstore:detail_view', product.id)

    return render(request, 'product_edit.html', {'form': product_form,
                                                'product': product})

@login_required
def merch_cart(request):
    user = Profile.objects.get(user=request.user)
    user_bought = Transaction.objects.filter(buyer=user)
    return render(request, 'cart.html', {'transactions':user_bought})

@login_required
def merch_transactions(request):
    user = Profile.objects.get(user=request.user)
    products = Transaction.objects.filter(product__owner=user)
    return render(request, 'transactions.html', {'transactions':products})
