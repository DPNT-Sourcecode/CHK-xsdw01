# -*- coding: utf-8 -*-
import unittest
from solutions.CHK import checkout_solution as C


class TestSum(unittest.TestCase):
    def test_checkout_abc(self):
        self.assertEqual(C.checkout('ABC'), 100)

    def test_checkout_deal_one(self):
        self.assertEqual(C.checkout('AAA'), 130)

    def test_checkout_deal_two(self):
        self.assertEqual(C.checkout('BB'), 45)

    def test_checkout_combination(self):
        """ Test should contain one 'AAA' deal, one 'BB' deal
            as well as an extra 'A', 'B', and one 'C' """
        self.assertEqual(C.checkout('AABACBA'), 275)

    def test_checkout_d(self):
        self.assertEqual(C.checkout('DD'), 30)

    def test_checkout_illegal_int(self):
        with self.assertRaises(TypeError):
            C.checkout(12)

    def test_checkout_illegal_float(self):
        with self.assertRaises(TypeError):
            C.checkout(1.0)

    def test_checkout_illegal_item(self):
        with self.assertRaises(ValueError):
            C.checkout('Z')


if __name__ == '__main__':
    unittest.main()
