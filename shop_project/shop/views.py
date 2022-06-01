from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from products.models import Product
from django.db.models import Q

def about_us(request):
    products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
    try:
        product_of_the_day = Product.objects.get(product_of_the_day=True)
    except:
        product_of_the_day = None
    context = {'form':AuthenticationForm(), 'product_of_the_day':product_of_the_day,
               'products_sale':products_sale,}
    return render(request,'about_us.html',context)
