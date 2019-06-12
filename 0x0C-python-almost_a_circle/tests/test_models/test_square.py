""" Module test rectangle """
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        f1 = "models/square.py"
        f2 = "tests/test_models/test_square.py"
        fchecker = pep8.Checker(f1, show_source=True)
        f2check = pep8.Checker(f2, show_source=True)
        file_errors = fchecker.check_all()
        file_errors_2 = f2check.check_all()


class TestSquareWorking(unittest.TestCase):
    """ class test rectangle """

    def setUp(self):
        """ setUp """
        self.s1 = Square(10)
        self.s2 = Square(2)
        self.s3 = Square(2, 1, 3, 12)

    def tearDown(self):
        """ TearDown """
        pass

    @classmethod
    def setUpClass(cls):
        """ set Up """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        pass

    def test_squ_normal(self):
        """ Normal cases """
        self.assertEqual(self.s1.id, 69)
        self.assertEqual(self.s2.id, 70)
        self.assertEqual(self.s3.id, 12)
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 2)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s3.x, 1)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 3)

    def test_size_zero(self):
        """ 0 width argument case """
        with self.assertRaises(ValueError):
            self.s1.size = 0

    def test_no_args(self):
        """No arguments cases """
        with self.assertRaises(TypeError):
            self.s1.size = 'H'

    def test_area_Rec_nor(self):
        """ Test Area """
        self.s1.size = 3
        self.assertEqual(self.s1.area(), 9)
        self.s1.size = 2
        self.assertEqual(self.s1.area(), 4)
        self.s1.size = 8
        self.assertEqual(self.s1.area(), 64)
