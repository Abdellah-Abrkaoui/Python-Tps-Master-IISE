import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.math_operations import addition, soustraction, multiplication, division
from src.string_operations import concat, upper_case

class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 4), 6)
        self.assertEqual(soustraction(5, 10), -5)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 4), 12)
        self.assertEqual(multiplication(-2, 3), -6)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    def test_concate(self):
        self.assertEqual(concat("abde", "ellah"), "abdellah")
        self.assertEqual(concat("Master", "2025"), "Master2025")
    
    def test_concate(self):
        self.assertEqual(upper_case("master"), "MASTER")
        self.assertEqual(upper_case("hello"), "HELLO")

        


if __name__ == '__main__':
    unittest.main()
