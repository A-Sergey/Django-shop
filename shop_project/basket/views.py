from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .basket import Basket
from .forms import BasketAddProductForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm


@require_POST
def basket_add(request, name):
    basket = Basket(request)
    product = get_object_or_404(Product, name=name)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['quantity'] == 0:
            basket_remove(request,name)
            return redirect(request.META['HTTP_REFERER'])
        basket.add(product=product,
                   quantity=cd['quantity'],
                   update_quantity=cd['update'])
    else:
        basket.add(product=product,
                   quantity=1,
                   update_quantity=False)
    return redirect(request.META['HTTP_REFERER'])

def basket_clear(request, name):
    basket = Basket(request)
    basket.clear()
    return HttpResponseRedirect(reverse("product",args=[name]))

def basket_remove(request,name):
    basket = Basket(request)
    product = get_object_or_404(Product, name=name)
    basket.remove(product)
    return redirect(request.META['HTTP_REFERER'])
    #return HttpRe.sponseRedirect(reverse("basket",args=[name]))

def basket_detail(request):
    basket = Basket(request)
    products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
    try:
        product_of_the_day = Product.objects.get(product_of_the_day=True)
    except:
        product_of_the_day = None
    if request.method == 'POST':
        basket_form = BasketAddProductForm(request.POST)
    else:
        basket_form = BasketAddProductForm()
    total = 0
    for product in basket:
        total += product['total_price']
    return render(request, 'basket.html', {'basket':basket,
                                           'products_sale':products_sale,
                                           'product_of_the_day':product_of_the_day,
                                           'basket_form':basket_form,
                                           'total':total,
                                           'form':AuthenticationForm(),})