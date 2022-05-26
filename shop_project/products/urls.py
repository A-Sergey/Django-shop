from .views import products,product
from django.urls import path, re_path, include



urlpatterns = [
    re_path(r'^$', products, name='products'),
    re_path(r'^(?P<name>\D+)/',product),
    #re_path(r'^(?P<name>\D+)/', product,{'document_root': settings.MEDIA_ROOT}),
]