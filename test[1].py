import unittest
from cal import sum_numbers

class TestNumberSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_numbers(2, 3), 5)
        self.assertEqual(sum_numbers(-1, 1), 1)
        self.assertEqual(sum_numbers(-1, -1), -2)

    def test_float(self):
        self.assertAlmostEqual(sum_numbers(2.5, 3.5), 6.0)
        self.assertAlmostEqual(sum_numbers(-1.5, 1.5), 2)

    def test_error(self):
        with self.assertRaises(TypeError):
            sum_numbers('a', 2)

if __name__ == "__main__":
    unittest.main()
