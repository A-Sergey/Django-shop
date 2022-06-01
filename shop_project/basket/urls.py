from .views import basket_add, basket_remove, basket_detail, basket_clear
from django.urls import path
import products.urls

urlpatterns = [
    path('', basket_detail),
    path('add/<name>/', basket_add, name="basket_add"),
    path('clear/<name>/', basket_clear, name='basket_clear'),
    path('remove/<name>/', basket_remove, name='basket_remove'),
]