import unittest

from main import min_of_three_vars


class MinOfThreeVarsTestCase(unittest.TestCase):

    def test_min_a(self):
        self.assertEqual(min_of_three_vars(1, 2, 3), 1)

    def test_min_b(self):
        self.assertEqual(min_of_three_vars(2, 1, 3), 1)

    def test_min_c(self):
        self.assertEqual(min_of_three_vars(3, 2, 1), 1)
