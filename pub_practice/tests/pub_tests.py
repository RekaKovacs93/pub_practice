import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("A Lady Lost", 1000)
        self.drink = Drink("Blue Moon", 2)
        self.customer01 = Customer("Spiderman", 100, 28)
        self.customer02 = Customer("Yousef", 0, 1)
        

    def test_pub_has_name(self):
        self.assertEqual("A Lady Lost", self.pub.name)

    def test_pub_can_sell_drink(self):
        self.pub.sell_a_drink(self.customer01, self.drink)
        self.assertEqual(1002, self.pub.till)
        self.assertEqual(98, self.customer01.wallet)

    def test_customer_age_old_enough(self):




    def test_customer_age_too_young(self):


