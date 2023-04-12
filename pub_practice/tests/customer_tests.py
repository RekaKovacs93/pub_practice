import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Spiderman", 100)

    def test_customer_has_name(self):
        self.assertEqual("Spiderman", self.customer.name)

        