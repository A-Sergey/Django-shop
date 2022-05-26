from .models import Product
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm
from django.contrib import auth
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from django.contrib.auth.forms import AuthenticationForm
from basket.forms import BasketAddProductForm

def products(request):
    list_products = Product.objects.all()
    context = {'list_products':list_products,'form':AuthenticationForm(),}
    return render(request,'products.html',context)

def product(request, name):
    product = get_object_or_404(Product, name=name)
    comments = product.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = auth.get_user(request)
            new_comment.save()
    else:
        comment_form = CommentForm()
    print('>>>>',product.image)
    return render(request, 'product.html', {'product': product,
                                            'comments':comments,
                                            'comment_form':comment_form,
                                            'form':AuthenticationForm()},)

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    basket_product_form = BasketAddProductForm()
    return render(request,'products.html', {'product':product,
                                            'basket_product_form': basket_product_form})