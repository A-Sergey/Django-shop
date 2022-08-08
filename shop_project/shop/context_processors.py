from products.models import Product
from cart.cart import Cart
from django.contrib.auth.forms import AuthenticationForm
from products.forms import FindProduct
from django.db.models import Q


def menu(request):
    names_menu = {"/": "Новости", "/products/": "Продукты", "/about_us/": "О нас"}
    return {"names_menu": names_menu}


def page_objects(request):
    try:
        product_of_the_day = Product.objects.get(product_of_the_day=True)
    except Product.DoesNotExist:
        product_of_the_day = None
    products_sale = Product.objects.filter(
        ~Q(sell="") & Q(product_of_the_day=False)
    )
    cart = Cart(request)
    total = 0
    for product in cart:
        total += product["total_price"]

    return {
        "product_of_the_day": product_of_the_day,
        "products_sale": products_sale,
        "form": AuthenticationForm(),
        "find_form": FindProduct(),
        "total": total,
    }
