#!/usr/bin/python3
""" Module test rectangle """
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestCodeFormat(unittest.TestCase):
    """ Class test for pep8 rectangle """

    def test_pep8_conformance(self):
        """ test pep8 """
        fchecker = pep8.Checker("models/square.py", show_source=True)
        file_errors = fchecker.check_all()

class TestSquareWorking(unittest.TestCase):
    """ class test rectangle """

    def test_squ_normal(self):
        """ Normal cases """
        s1 = Square(10, 0, 0, 1)
        self.assertEqual(s1.id, 1)
        s2 = Square(2, 0, 0, 2)
        self.assertEqual(s2.id, 2)
        s3 = Square(2, 0, 0, 12)
        self.assertEqual(s3.id, 12)
        s4 = Square(4, 5, 6, 7)
        self.assertEqual(s4.size, 4)
        s5 = Square(2, 3, 4, 8)
        self.assertEqual(s5.size, 2)
        self.assertEqual(s5.x, 3)
        self.assertEqual(s5.y, 4)
        self.assertEqual(s5.id, 8)

    def test_arg_one(self):
        """ one argument case """
        s6 = Square(1)
        self.assertEqual(s6.size, 1)

    def test_size_zero(self):
        """ 0 width argument case """
        with self.assertRaises(ValueError):
            s7 = Square(0)

    def test_no_args(self):
        """No arguments cases """
        with self.assertRaises(TypeError):
            s8 = Square()

    def test_x_neg(self):
        """ Negative x """
        with self.assertRaises(ValueError):
            s9 = Square(1, 2, -1, 8)

    def test_y_neg(self):
        """ Negative y """
        with self.assertRaises(ValueError):
            s10 = Square(1, -2, 1, 1)

    def test_width_wr_type(self):
        """ String width """
        with self.assertRaises(TypeError):
            s11 = Square('A', 1, -1)

    def test_height_wr_type(self):
        """ String height """
        with self.assertRaises(TypeError):
            s12 = Square(1, 'H', 1, 0)

    def test_x_wr_type(self):
        """ String x """
        with self.assertRaises(TypeError):
            s13 = Square(1, 2, 'A', 0)

    def test_y_wr_type(self):
        """ String y """
        with self.assertRaises(TypeError):
            s14 = Square(1, 'h', 1, 0)

    def test_float_Rec(self):
        """ float numbers """
        with self.assertRaises(TypeError):
            s15 = Square(2.5, 3, 4, 5, 9)

    def test_area_Rec_nor(self):
        """ Test Area """
        s16 = Square(3)
        self.assertEqual(s16.area(), 9)
        s17 = Square(2)
        self.assertEqual(s17.area(), 4)
        s18 = Square(8)
        self.assertEqual(s18.area(), 64)



if __name__ == '__main__':
    unittest.main()
