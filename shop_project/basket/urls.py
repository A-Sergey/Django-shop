from .views import basket_add, basket_remove, basket_detail
from django.urls import path
import products.urls

urlpatterns = [
    path('', basket_detail),
    path('add/<int:product_id>', basket_add, name="basket_add"),
    path('remove/<int:product_id>', basket_remove),
]