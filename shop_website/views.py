from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from shop_website.models import Category, Product, Comment
from typing import Optional
from shop_website.forms import CommentModelForm, OrderModelForm

# Create your views here.
def product_list(request, category_id: Optional[int]=None ):
    categories=Category.objects.all().order_by('id')
    if category_id:
        products=Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()
    context={
    'products': products,
    'categories': categories } 
    return render (request, 'shop_website/home.html', context)

def product_details (request, product_id):
    product=Product.objects.get(id=product_id)
    comments=Comment.objects.filter(product=product_id, is_provided=True).order_by('-id')
    context={
        'product': product,
        'comments': comments
        }
    return render (request, 'shop_website/detail.html', context)


# def add_comment(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        user_comment=Comment(name=name, email=email, comment=comment)
        user_comment.product=product
        user_comment.save()
        return redirect ('product_details', product_id)
    else:
        pass
    return render(request, 'shop_website/detail.html')

def add_comment(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    if request.method=='POST':
        form=CommentModelForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.product=product
            comment.save()
            return redirect('product_details', product_id)
    else:
        form=CommentModelForm()
    context={
        'form':form,
        'product': product
    }

    return render(request, 'shop_website/detail.html', context )

def place_order(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    if request.method=='POST':
        form=OrderModelForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.product=product
            order.save()
            return redirect('product_details', product_id)
    else:
        form=OrderModelForm()
    context={
        'form':form,
        'product': product
    }

    





