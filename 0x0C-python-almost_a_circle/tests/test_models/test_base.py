#!/usr/bin/python3
""" Module test for base"""
import unittest
import pep8
from models.base import Base


class TestCodeFormat(unittest.TestCase):
    """ class test for pep8 """

    def test_pep8_conformance(self):
        """ test pep8 """
        fchecker = pep8.Checker("models/base.py", show_source=True)
        file_errors = fchecker.check_all()

class TestBaseWorking(unittest.TestCase):
    """ Class test for base """

    def setUp(self):
        """ setUp """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def tearDown(self):
        """ TearDown"""
        pass

    def test_base_normal(self):
        """ normal cases test """
        self.assertEqual(self.b1.id, 17)
        self.assertEqual(self.b2.id, 18)
        self.assertEqual(self.b3.id, 19)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 20)

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
