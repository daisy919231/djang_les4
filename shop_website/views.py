from django.shortcuts import render, HttpResponse
from shop_website.models import Category, Product, Comment
from typing import Optional

# Create your views here.
def product_list(request):
    categories=Category.objects.all()
    products = Product.objects.all()
    context={
    'products': products,
    'categories': categories } 
    return render (request, 'shop_website/home.html', context)

def product_details (request, product_id):
    product=Product.objects.get(id=product_id)
    context={
        'product': product
        }
    return render (request, 'shop_website/detail.html', context)
