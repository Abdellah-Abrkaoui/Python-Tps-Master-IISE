# tests unitaires pour le module "conversion.py"

import unittest
from conversion import dollars_to_dirhams, meters_to_kilometers

class TestConversion(unittest.TestCase):
    # dollars to mad unittest
    def test_dollars_to_dirhams(self):
        self.assertEqual(dollars_to_dirhams(10),100)
        with self.assertRaises(ValueError):
            dollars_to_dirhams(-10)

    # meters to km unittest
    def test_meters_to_kilometers(self):
        self.assertEqual(meters_to_kilometers(1000),1)
        with self.assertRaises(ValueError):
            meters_to_kilometers(-10)


if __name__ == "__name__":
    unittest.main()



# run using command : python -m unittest test_conversion.py