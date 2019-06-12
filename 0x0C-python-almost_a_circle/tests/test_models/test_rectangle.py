""" Module test rectangle """
import unittest
import pep8
import sys
from models.base import Base
from models.rectangle import Rectangle


def setUpModule():
    """ set Up """
    pass


def tearDownModule():
    """ Tear Down"""
    pass


class TestCodeFormat(unittest.TestCase):
    """ class test for pep8 """

    def test_pep8_conformance(self):
        """ test pep8 """
        stl = pep8.StyleGuide(quiet=True)
        f1 = "models/rectangle.py"
        f2 = "tests/test_models/test_rectangle.py"
        fchecker = pep8.Checker(f1, show_source=True)
        f2check = pep8.Checker(f2, show_source=True)
        file_errors = fchecker.check_all()
        file_errors_2 = f2check.check_all()


class TestRectangleWorking(unittest.TestCase):
    """ class test rectangle """

    def setUp(self):
        """ setUp """
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        """ TearDown """
        Base.__nb_objects = None

    @classmethod
    def setUpClass(cls):
        """ set Up """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        pass

    def test_rec_id(self):
        """ Normal cases """
        self.assertEqual(self.r1.id, 51)
        self.assertEqual(self.r2.id, 52)
        self.assertEqual(self.r3.id, 12)

    def test_rec_width(self):
        """ width cases """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_rec_height(self):
        """ Height cases """
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

    def test_rec_x(self):
        """ x cases """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 0)

    def test_rec_y(self):
        """ y cases """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)

    def test_update(self):
        self.r2.update(89)
        self.assertEqual(self.r2.id, 89)
        self.r2.update(89, 2)
        self.assertEqual(self.r2.width, 2)
        self.r2.update(89, 2, 3)
        self.assertEqual(self.r2.height, 3)
        self.r2.update(89, 2, 3, 4)
        self.assertEqual(self.r2.x, 4)
        self.r2.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r2.y, 5)

    def test_update_2(self):
        self.r2.update(height=1)
        self.assertEqual(self.r2.height, 1)
        self.r2.update(width=1, x=2)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.x, 2)
        self.r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r2.id, 89)
        self.r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.y, 3)
        self.assertEqual(self.r2.width, 4)

    def test_fail_width_ty(self):
        with self.assertRaises(TypeError):
            self.r1.width = 'Hello'
            self.r2.width = ''
            self.r3.width = 2.5

    def test_fail_height_ty(self):
        with self.assertRaises(TypeError):
            self.r1.height = 'Hello'
            self.r2.height = ''
            self.r3.height = 'A'

    def test_fail_x_ty(self):
        with self.assertRaises(TypeError):
            self.r1.x = 'Hello'
            self.r2.x = ''
            self.r3.x = 'A'

    def test_fail_y_ty(self):
        with self.assertRaises(TypeError):
            self.r1.y = 'Hello'
            self.r2.y = ''
            self.r3.y = 'A'

    def test_fail_width_val(self):
        with self.assertRaises(ValueError):
            self.r1.width = -1
            self.r2.width = -2
            self.r3.width = -3

    def test_fail_height_val(self):
        with self.assertRaises(ValueError):
            self.r1.height = -4
            self.r2.height = -5
            self.r3.height = -6

    def test_fail_x_val(self):
        with self.assertRaises(ValueError):
            self.r1.x = -4
            self.r2.x = -5
            self.r3.x = -6

    def test_fail_y_val(self):
        with self.assertRaises(ValueError):
            self.r1.y = -4
            self.r2.y = -5
            self.r3.y = -6
