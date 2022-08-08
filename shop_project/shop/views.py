from django.shortcuts import redirect, render
from django.urls import reverse
from products.models import Product
from django.db.models import Q


def about_us(request):
    context = {}
    return render(request, "about_us.html", context)
