#!/usr/bin/python3
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        fchecker = pep8.Checker("models/rectangle.py", show_source=True)
        file_errors = fchecker.check_all()

class TestBaseWorking(unittest.TestCase):

    def test_rec_normal(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(r4.height, 4)
        r5 = Rectangle(1, 2, 3, 4, 8)
        self.assertEqual(r5.width, 1)
        self.assertEqual(r5.x, 3)
        self.assertEqual(r5.y, 4)
        self.assertEqual(r5.id, 8)

    def test_arg_one(self):
        with self.assertRaises(TypeError):
            r6 = Rectangle(1)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 1)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(1, 0)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle()

    def test_x_neg(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(1, 2, -1, 2)

    def test_y_neg(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(1, 2, 1, -1)

    def test_width_wr_type(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle('A', 2, 1, -1)

    def test_height_wr_type(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 'H', 1, 0)

    def test_x_wr_type(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 'A', 0)

    def test_y_wr_type(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 1, 'H')

    def test_float_Rec(self):
        with self.assertRaises(TypeError):
            r7 = Rectangle(2.5, 3, 4, 5, 9)

    def test_area_Rec_nor(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)



if __name__ == '__main__':
    unittest.main()
