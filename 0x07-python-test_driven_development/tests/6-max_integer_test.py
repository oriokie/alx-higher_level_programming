#!/usr/bin/python3
"""
Test Module for the 6-max_integer module

"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMax(unittest.TestCase):
    def test_regular(self):
        self.assertTrue(max_integer([1, 2, 3, 4]), 4)

    def test_negative(self):
        self.assertTrue(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_float(self):
        self.assertTrue(max_integer([1.2, 2.3, 3.4, 4.5]), 4.5)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_strings(self):
        my_list = ["a", 4, 3, 1]
        with self.assertRaises(TypeError):
            max_integer(my_list)

if __name__ == "__main__":
    unittest.main()
