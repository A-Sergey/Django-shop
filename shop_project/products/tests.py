from django.test import TestCase
from products.models import Product


class ProducTest(TestCase):
    def test_str(self):
        product = Product(name="Meal", price="5")
        self.assertEqual(str(product), "Meal=5 руб")
