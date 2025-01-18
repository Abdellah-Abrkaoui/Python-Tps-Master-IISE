import unittest

from exercice_1 import safe_division
from exercice_2 import convert_to_int

class TestExceptions(unittest.TestCase):
    def test_division_error(self):
        self.assertEqual(safe_division(10,2),5)
        with self.assertRaises(ZeroDivisionError):
            safe_division(10,0)

    
    def test_convert_to_int(self):
        self.assertEqual(convert_to_int("18"), 18)
        with self.assertRaises(ValueError):
            convert_to_int("abc")



if __name__ == '__main__':
    unittest.main()
