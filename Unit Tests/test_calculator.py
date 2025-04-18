import unittest
from calculator import add, subtract, multiply, divide, power

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5) #This test checks if the output would = to 5
    
    def test_add_negative_numbers_together(self):
       self.assertEqual(add(-5, -3), -8) #This test checks if output = to -8
       
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2) #Test checks if output = 2

    def test_subtract_answer_equals_negative(self):
       self.assertEqual(subtract(0, 2), -2) # Test checks if output = -2
    
    def test_multiply(self):
        self.assertEqual(multiply(11,5), 55) #Test checks if output = 55
    
    def test_divide(self): 
     self.assertEqual(divide(9,3), 3) #Test check output = 3

    def test_divide_raise_valueError(self):
       with self.assertRaises(ZeroDivisionError):
        divide(10,0)
    
    def test_exponentation(self):
       self.assertEqual(power(3,3), 27) #Test check output = 27

#Run tests
unittest.main()
