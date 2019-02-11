import unittest
import array as arr
from multiples import *


class EvenNumbers(unittest.TestCase):

    def test_multiply_even_numbers(self):
        mylist = arr.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print (mylist)
        multiplication_even=even_elements_mult(mylist)
        print ("6758476748678573456########7584367347864376")
        print (multiplication_even)
        #self.assertEqual(384, multiplication_even(384))