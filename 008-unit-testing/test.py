import unittest

from app import *

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1,2), 3, msg=True)

    def test_addition_incorrect(self):
        self.assertNotEqual(add(2,3), 6, msg=True)

    def test_subtraction(self):
        self.assertEqual(sub(3,2), 1, msg=True)

    def test_subtraction_incorrect(self):
        self.assertNotEqual(sub(3,1), 3, msg=True)

    def test_multiplication(self):
        self.assertEqual(mul(2,3), 6, msg=True)

    def test_multiplication_incorrect(self):
        self.assertNotEqual(mul(4,3), 2, msg=True)

    def test_division(self):
        self.assertEqual(div(4,2), 2, msg=True)

    def test_division_incorrect(self):
        self.assertNotEqual(div(2,3), 1, msg=True)