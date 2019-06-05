

import unittest
from class_operations import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
   
    def test_add(self):
        self.assertEqual(4, self.calculator.Add(2,2))
        self.assertEqual(3.2, self.calculator.Add(2,1.2))

    def test_minus(self):
        self.assertEqual(2, self.calculator.Subtract(4,2))
        self.assertEqual(-2, self.calculator.Subtract(2,4))

    def test_multiple(self):
        self.assertEqual(12, self.calculator.Multiplication(6,2))
        self.assertEqual(13.2, self.calculator.Multiplication(11,1.2))

    def test_divide(self):
        self.assertEqual(3, self.calculator.Division(3,1))
		
if __name__ == "__main__":
	unittest.main() 