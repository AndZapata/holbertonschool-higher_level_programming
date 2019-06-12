""" Module test for base"""
import unittest
import pep8
import sys
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
        f1 = "models/base.py"
        f2 = "tests/test_models/test_base.py"
        fchecker = pep8.Checker(f1, show_source=True)
        f2check = pep8.Checker(f2, show_source=True)
        file_errors = fchecker.check_all()
        file_errors_2 = f2check.check_all()


class TestBaseWorking(unittest.TestCase):
    """ Class test for base """

    def setUp(self):
        """ set Up """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        """ Tear Down"""
        self.__nb_objects = None

    @classmethod
    def setUpClass(cls):
        """ set Up """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Tear down class """
        pass

    def test_base_id(self):
        """ normal cases test """
        self.assertEqual(self.b1.id, 5)
        self.assertEqual(self.b2.id, 6)
        self.assertEqual(self.b3.id, 7)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 8)

    def test_base_zero(self):
        """ zero case """
        self.b1 = Base(0)
        self.assertEqual(self.b1.id, 0)

    def test_base_neg(self):
        """ negative case """
        self.b1 = Base(-4)
        self.assertEqual(self.b1.id, -4)

    def test_base_neg_float(self):
        """ negative floating case """
        self.b1 = Base(-3.4)
        self.assertEqual(self.b1.id, -3.4)

    def test_base_str(self):
        """ String case """
        self.b1 = Base('Hello')
        self.assertEqual(self.b1.id, 'Hello')

    def test_base_list(self):
        """ List case """
        self.b1 = Base([1, 2, 3, 4])
        self.assertEqual(self.b1.id, [1, 2, 3, 4])

    def test_base_tup(self):
        """ Tuple case """
        self.b1 = Base((1, 2))
        self.assertEqual(self.b1.id, (1, 2))

    def test_base_dir(self):
        """ Dictionary case """
        self.b1 = Base({'A': 1, 'B': 2})
        self.assertEqual(self.b1.id, {'A': 1, 'B': 2})

if __name__ == '__main__':
    unittest.main()
