import unittest

from exercises.multiples import *



class MultipleTestSuite(unittest.TestCase):

    def test_multiples(self):
        self.assertEqual(23, sum_elements(10))

    def test_good(self):
        self.assertEqual(False, good(0))
        self.assertEqual(False, good(1))
        self.assertEqual(False, good(2))
        self.assertEqual(True, good(3))
        self.assertEqual(False, good(4))
        self.assertEqual(True, good(5))
        self.assertEqual(True, good(6))
        self.assertEqual(False, good(7))
        self.assertEqual(False, good(8))
        self.assertEqual(True, good(9))

