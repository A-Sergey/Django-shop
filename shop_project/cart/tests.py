from django.test import TestCase
from cart.cart import Cart
from products.models import Product

class CartTest(TestCase):
        cart = Cart()
        product_without_sell = Product(name='TestProduct', price='99',
                                        description='TestDescription')
        product_with_sell = Product(name='TestProduct', price='99', sell='55',
                                    description='TestDescription')
        product_without_sell.comments

