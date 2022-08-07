from django.urls import path
from .views import cart_add, cart_remove, cart_detail, cart_clear

urlpatterns = [
    path('', cart_detail),
    path('add/<name>/', cart_add, name="cart_add"),
    path('clear/<name>/', cart_clear, name='cart_clear'),
    path('remove/<name>/', cart_remove, name='cart_remove'),
]