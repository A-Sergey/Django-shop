from .models import Product
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm
from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm
from basket.basket import Basket
from basket.forms import BasketAddProductForm

def products(request):
    basket = Basket(request)
    list_products = Product.objects.all()
    products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
    try:
        product_of_the_day = Product.objects.get(product_of_the_day=True)
    except:
        product_of_the_day = None
    if request.method == 'POST':
        basket_form = BasketAddProductForm(request.POST)
        if basket_form.is_valid():
            pass
        return redirect(request.META['HTTP_REFERER'])
    else:
        basket_form = BasketAddProductForm(initial={'quantity':0})
    for product in list_products:
        product.id = str(product.id)
    context = {'list_products':list_products,'basket':basket,'form':AuthenticationForm(),
               'basket_form':basket_form,'product_of_the_day':product_of_the_day,
               'products_sale':products_sale,}
    return render(request,'products.html',context)

def product(request, name):
    product = get_object_or_404(Product, name=name, )
    try:
        product_of_the_day = Product.objects.get(product_of_the_day=True)
    except:
        product_of_the_day = None
    comments = product.comments.filter(active=True)
    comments = comments.order_by('-created')
    products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
    print(products_sale)
    basket = Basket(request)
    dict_count = {}
    count = len(comments)+1
    for comment in comments:
        count -=1
        dict_count.update({comment.id:count})
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        basket_form = BasketAddProductForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = auth.get_user(request)
            new_comment.save()
        if basket_form.is_valid():
            pass
        return HttpResponseRedirect(reverse("product",args=[name]))
    else:
        comment_form = CommentForm()
        comment_form.cleanquantity = 0
        try:
            quantity = basket.basket[str(product.id)]['quantity']
            basket_form = BasketAddProductForm(initial={'quantity':quantity})
        except KeyError:
            basket_form = BasketAddProductForm(initial={'quantity':0})
    paginator = Paginator(comments,5,orphans=1)
    page = request.GET.get('page')
    
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments= paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    
    return render(request, 'product.html', {'product': product,
                                            'products_sale': products_sale,
                                            'comments':comments,
                                            'basket':basket,
                                            'dict_count':dict_count,
                                            'comment_form':comment_form,
                                            'basket_form':basket_form,
                                            'form':AuthenticationForm(),
                                            'product_of_the_day':product_of_the_day,},)