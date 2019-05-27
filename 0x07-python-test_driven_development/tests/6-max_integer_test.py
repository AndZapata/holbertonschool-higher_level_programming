#!/usr/bin/python3
""" Unittest for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_val_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_val_mid(self):
        self.assertEqual(max_integer([4, 5, 7, 6, 3]), 7)

    def test_max_val_first(self):
        self.assertEqual(max_integer([9, 5, 4, 3, 2]), 9)

    def test_one_arg_pos(self):
        self.assertEqual(max_integer([9]), 9)

    def test_one_arg_neg(self):
        self.assertEqual(max_integer([-2]), -2)

    def test_one_arg_none(self):
        self.assertEqual(max_integer([]), None)

    def test_only_neg(self):
        self.assertEqual(max_integer([-1, -4, -5, -6, -99, -5]), -1)

    def test_float(self):
        self.assertEqual(max_integer([5.7, 6.8, 9.1, 9.3]), 9.3)

    def test_TE_no_args(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 1, 2])

if __name__ == '__main__':
    unittest.main()
