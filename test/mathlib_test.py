import unittest
from src.mathlib import Operations


class OperationsTests(unittest.TestCase):
    def test_valid_sum(self):
        self.assertEqual(Operations.sum(3, 4), 7)

    def test_invalid_sum(self):
        self.assertFalse(Operations.sum(2.0, 3.0), 5.0)

