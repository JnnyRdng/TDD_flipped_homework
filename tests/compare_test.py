import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_6_3_returns_6_is_greater_than_3(self):
        self.assertEqual("6 is greater than 3", compare(6, 3))