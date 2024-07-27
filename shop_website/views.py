from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render (request, 'shop_website/home.html')

def product_details (request):
    return render (request, 'shop_website/detail.html' )