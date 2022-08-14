from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from cart.cart import Cart
from cart.forms import CartAddProductForm
from .forms import CommentForm, FindProduct
from .models import Product


def products(request):
    cart = Cart(request)
    list_products = Product.objects.filter(visible_in_shop=True)
    if request.method == "POST":
        cart_form = CartAddProductForm(request.POST)
        if cart_form.is_valid():
            return redirect(request.META["HTTP_REFERER"])
    else:
        cart_form = CartAddProductForm(initial={"quantity": 0})
    for product in list_products:
        product.id = str(product.id)
    paginator = Paginator(list_products, 6)
    page = request.GET.get("page")
    try:
        list_products = paginator.page(page)
    except PageNotAnInteger:
        list_products = paginator.page(1)
    except EmptyPage:
        list_products = paginator.page(paginator.num_pages)
    context = {
        "list_products": list_products,
        "cart": cart,
        "cart_form": cart_form,
    }
    return render(request, "products.html", context)


def product(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
    )
    comments = product.comments.filter(active=True)
    comments = comments.order_by("-created")
    cart = Cart(request)
    dict_count = {}
    count = len(comments) + 1
    try:
        editable_comment_id = int(request.GET.get("editable_comment_id"))
    except TypeError:
        editable_comment_id = None
    for comment in comments:
        count -= 1
        dict_count.update({comment.id: count})
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        cart_form = CartAddProductForm(request.POST)
        if editable_comment_id:
            comment = product.comments.get(id=editable_comment_id)
            edit_comment = request.POST.get("edit_comment")
            if (request.user == comment.author) and (comment.product == product):
                comment.body = edit_comment
                comment.save()
                return redirect(
                    f"/products/{product.slug}/want#{editable_comment_id}"
                )

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = auth.get_user(request)
            new_comment.save()
        return redirect(f"/products/{product.slug}/")
    else:
        comment_form = CommentForm()
        try:
            quantity = cart.cart[str(product.id)]["quantity"]
            cart_form = CartAddProductForm(initial={"quantity": quantity})
        except KeyError:
            cart_form = CartAddProductForm(initial={"quantity": 0})
    paginator = Paginator(comments, 5, orphans=1)
    page = request.GET.get("page")
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(
        request,
        "product.html",
        {
            "product": product,
            "comments": comments,
            "cart": cart,
            "dict_count": dict_count,
            "comment_form": comment_form,
            "cart_form": cart_form,
            "editable_comment_id": editable_comment_id,
        },
    )


def find_product(request):
    if request.method == "POST":
        find_form = FindProduct(request.POST)
        if find_form.is_valid():
            cd = find_form.cleaned_data
            product_find = Product.objects.filter(
                name_lower__icontains = cd["find_product"]
            )
            if product_find:
                if len(product_find) == 1:
                    return redirect(f"/products/{product_find[0].slug}/")
    else:
        find_form = FindProduct()
        return redirect(request.META["HTTP_REFERER"])
    return render(
        request,
        "find.html",
        {
            "product_find": product_find,
        },
    )
