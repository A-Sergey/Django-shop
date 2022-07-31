from django.urls import re_path
from .views import products,product,find_product

urlpatterns = [
    re_path(r'^$', products, name='products'),
    re_path(r'^find/',find_product, name='find_product'),
    re_path(r'^(?P<name>\w+)/',product, name='product'),   
]

