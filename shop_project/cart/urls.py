from django.urls import path
from .views import cart_add, cart_remove, cart_detail, cart_clear

urlpatterns = [
    path("", cart_detail),
    path("add/<slug>/", cart_add, name="cart_add"),
    path("clear/<slug>/", cart_clear, name="cart_clear"),
    path("remove/<slug>/", cart_remove, name="cart_remove"),
]
