from django.test import TestCase
from products.models import Product


class ProducTest(TestCase):
    """Product model tests."""

    def test_str(self):
        product = Product(name="Meal", price="5")
        self.assertEqual(str(product), "Meal=5 руб")
