import unittest
import array as arr
from multiples import *


class EvenNumbers(unittest.TestCase):

    def test_multiply_even_numbers(self):
        x = [i for i in range(10)]
        multiplication_even=even_elements_mult(x)
        print (multiplication_even)
        #self.assertEqual(384, multiplication_even(384))