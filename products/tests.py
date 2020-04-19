from django.test import TestCase
from .models import Product
# Create your tests here.

class ProductTest(TestCase):
    """
    Here we will define our tests
    the tests will be run against our product model
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')

