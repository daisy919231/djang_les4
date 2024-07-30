from django.shortcuts import render
from shop_website.models import Category, Product, Comment

# Create your views here.
def product_list(request):
    return render (request, 'shop_website/home.html')

def product_details (request):
    products = Product.objects.all()
    context={
        'products': products } 
    return render (request, 'shop_website/detail.html', context )

def categories(request):
    categories = Category.objects.all()
    context={
        'categories': categories  
        }
    return render (request, 'shop_website.home.html', context)

def comments(request):
    comments=Comment.objects.all()
    context={
        "comments": comments
    }
    return render (request, 'shop_website/detail.html', context )

# def products(request):
#     products = Product.objects.all()
#     context={
#         'products': products  
#         }
#     return render (request, 'shop_website.home.html', context)