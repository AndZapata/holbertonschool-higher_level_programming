#!/usr/bin/python3
import unittest
import pep8
from models.base import Base


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        fchecker = pep8.Checker("models/base.py", show_source=True)
        file_errors = fchecker.check_all()

class TestBaseWorking(unittest.TestCase):

    def test_base_normal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_base_zero(self):
        b6 = Base(0)
        self.assertEqual(b6.id, 0)

    def test_base_neg(self):
        b7 = Base(-4)
        self.assertEqual(b7.id, -4)

    def test_base_neg_float(self):
        b9 = Base(-3.4)
        self.assertEqual(b9.id, -3.4)

    def test_base_str(self):
        b8 = Base('Hello')
        self.assertEqual(b8.id, 'Hello')

    def test_base_list(self):
        b9 = Base([1, 2, 3, 4])
        self.assertEqual(b9.id, [1, 2, 3, 4])

    def test_base_tup(self):
        b9 = Base((1, 2))
        self.assertEqual(b9.id, (1, 2))

    def test_base_dir(self):
        b9 = Base({'A': 1, 'B': 2})
        self.assertEqual(b9.id, {'A': 1, 'B': 2})


if __name__ == '__main__':
    unittest.main()
