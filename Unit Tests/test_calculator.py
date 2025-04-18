import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5) #This test checks if the output would = to 5
    
    def test_subtract(sekf):
        self.assertEqual(subtract(5, 3), 2) #Test checks if output = 2
    
    def test_multiply(self):
        self.assertEqual(multiply(11,5), 55) #Test checks if output = 55
    
    def test_divide(self): 
     self.assertEqual(divide(9,3), 3) #Test check output = 3

    def test_divide_raise_valueError(self):
       self.assertRaises(ZeroDivisionError):
       divide(10,0)
