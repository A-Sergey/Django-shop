from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponseRedirect
from django.urls import reverse


@require_POST
def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd["quantity"] == 0:
            cart_remove(request, slug)
            return redirect(request.META["HTTP_REFERER"])
        if product.quantity >= cd["quantity"]:
            cart.add(
                product=product, quantity=cd["quantity"],
                update_quantity=cd["update"]
            )
        else:
            cart.add(
                product=product, quantity=product.quantity,
                update_quantity=cd["update"]
            )
    else:
        cart.add(product=product, quantity=1, update_quantity=False)
    return redirect(request.META["HTTP_REFERER"])


def cart_clear(request, slug):
    cart = Cart(request)
    cart.clear()
    return HttpResponseRedirect(reverse("product", args=[slug]))


def cart_remove(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.remove(product)
    return redirect(request.META["HTTP_REFERER"])


def cart_detail(request):
    cart = Cart(request)
    if request.method == "POST":
        cart_form = CartAddProductForm(request.POST)
    else:
        cart_form = CartAddProductForm()
    return render(
        request,
        "cart.html",
        {
            "cart": cart,
            "cart_form": cart_form,
        },
    )
