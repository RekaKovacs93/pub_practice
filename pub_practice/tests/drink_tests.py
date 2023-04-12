import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Appletizer", 2)

    def test_drink_has_name(self):
        self.assertEqual("Appletizer", self.drink.name)

