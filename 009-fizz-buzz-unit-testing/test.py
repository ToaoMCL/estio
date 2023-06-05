import unittest

from app import *

class TestCalculate(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz", msg=True)

    def test_fizz(self):
        self.assertEqual(fizzbuzz(9), "fizz", msg=True)

    def test_buzz(self):
        self.assertEqual(fizzbuzz(10), "buzz", msg=True)

    def test_not_fizz_buzz_or_fizzbuzz(self):
        self.assertEqual(fizzbuzz(4), "4", msg=True)