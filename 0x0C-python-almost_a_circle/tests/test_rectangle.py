#!/usr/bin/python3
""" Module test rectangle """
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestCodeFormat(unittest.TestCase):
    """ Class test for pep8 rectangle """

    def test_pep8_conformance(self):
        """ test pep8 """
        fchecker = pep8.Checker("models/rectangle.py", show_source=True)
        file_errors = fchecker.check_all()

class TestRectangleWorking(unittest.TestCase):
    """ class test rectangle """

    def test_rec_normal(self):
        """ Normal cases """
        r1 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10, 0, 0, 2)
        self.assertEqual(r2.id, 2)
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
        """ one argument case """
        with self.assertRaises(TypeError):
            r6 = Rectangle(1)

    def test_width_zero(self):
        """ 0 width argument case """
        with self.assertRaises(ValueError):
            r7 = Rectangle(0, 1)

    def test_height_zero(self):
        """ 0 height argument case """
        with self.assertRaises(ValueError):
            r8 = Rectangle(1, 0)

    def test_no_args(self):
        """No arguments cases """
        with self.assertRaises(TypeError):
            r9 = Rectangle()

    def test_x_neg(self):
        """ Negative x """
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, 2, -1, 2)

    def test_y_neg(self):
        """ Negative y """
        with self.assertRaises(ValueError):
            r11 = Rectangle(1, 2, 1, -1)

    def test_width_wr_type(self):
        """ String width """
        with self.assertRaises(TypeError):
            r12 = Rectangle('A', 2, 1, -1)

    def test_height_wr_type(self):
        """ String height """
        with self.assertRaises(TypeError):
            r13 = Rectangle(1, 'H', 1, 0)

    def test_x_wr_type(self):
        """ String x """
        with self.assertRaises(TypeError):
            r14 = Rectangle(1, 2, 'A', 0)

    def test_y_wr_type(self):
        """ String y """
        with self.assertRaises(TypeError):
            r15 = Rectangle(1, 2, 1, 'H')

    def test_float_Rec(self):
        """ float numbers """
        with self.assertRaises(TypeError):
            r16 = Rectangle(2.5, 3, 4, 5, 9)

    def test_area_Rec_nor(self):
        """ Test Area """
        r17 = Rectangle(3, 2)
        self.assertEqual(r17.area(), 6)
        r18 = Rectangle(2, 10)
        self.assertEqual(r18.area(), 20)
        r19 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r19.area(), 56)



if __name__ == '__main__':
    unittest.main()
