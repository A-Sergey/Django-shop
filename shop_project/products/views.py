from .models import Product
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm
from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.forms import AuthenticationForm
from basket.forms import BasketAddProductForm

def products(request):
    list_products = Product.objects.all()
    context = {'list_products':list_products,'form':AuthenticationForm(),}
    return render(request,'products.html',context)

def product(request, name):
    product = get_object_or_404(Product, name=name)
    comments = product.comments.filter(active=True)
    comments = comments.order_by('-created')
    dict_count = {}
    count = len(comments)+1
    for comment in comments:
        count -=1
        dict_count.update({comment.id:count})
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = auth.get_user(request)
            new_comment.save()
        return HttpResponseRedirect(reverse("product",args=[name]))
    else:
        comment_form = CommentForm()
        new_comment = None
    paginator = Paginator(comments,5,orphans=1)
    page = request.GET.get('page')
    
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments= paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    print(dict_count)
    return render(request, 'product.html', {'product': product,
                                            'comments':comments,
                                            'dict_count':dict_count,
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