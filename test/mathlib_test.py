import unittest
from src.mathlib import Operations


class OperationsTests(unittest.TestCase):
    def test_sum(self):
        # failed test
        self.assertEqual(Operations.sum(3, 4), 7)

