# -*- coding: utf-8 -*-
import unittest

from solutions.CHK import checkout_solution as C


class TestSum(unittest.TestCase):
    def test_checkout_abc(self):
        self.assertEqual(C.sum_basket('ABC'), 100)

    def test_checkout_deal_one(self):
        self.assertEqual(C.sum_basket('AAA'), 130)

    def test_checkout_deal_two(self):
        self.assertEqual(C.sum_basket('BB'), 45)

    def test_checkout_combination(self):
        """ Test should contain one 'AAA' deal, one 'BB' deal
            as well as an extra 'A', 'B', and one 'C' """
        self.assertEqual(C.sum_basket('AABACBA'), 275)

    def test_checkout_d(self):
        self.assertEqual(C.sum_basket('DD'), 30)

    def test_checkout_illegal_int(self):
        with self.assertRaises(TypeError):
            C.sum_basket(12)

    def test_checkout_illegal_float(self):
        wwith self.assertRaises(TypeError):
            C.sum_basket(1.0)

    def test_checkout_illegal_item(self):
        wwith self.assertRaises(ValueError):
            C.sum_basket('Z')


    # def test_hello_world(self):
    #     self.assertEqual(hello_solution.hello("World"),
    #                      "Hello, World!")
    #
    # def test_hello_john(self):
    #     self.assertEqual(hello_solution.hello("John"),
    #                      "Hello, John!")
    #
    # def test_hello_lower_case(self):
    #     self.assertEqual(hello_solution.hello("john"),
    #                      "Hello, john!")


if __name__ == '__main__':
    unittest.main()
