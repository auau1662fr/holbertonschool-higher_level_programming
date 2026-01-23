#!/usr/bin/python3
"""
Unittests for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 3, 2]), 5)

    def test_same_values(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)


if __name__ == "__main__":
    unittest.main()
