from django.test import TestCase
from basket.basket import Basket
from products.models import Product

class BasketTest(TestCase):
        basket = Basket()
        product_without_sell = Product(name='TestProduct', price='99',description='TestDescription')
        product_with_sell = Product(name='TestProduct', price='99', sell='55', description='TestDescription')
        product_without_sell.comments
    #def test_correct_vars(self):
        
        
    #def test_add(self):

        
        