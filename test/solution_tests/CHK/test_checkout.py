# -*- coding: utf-8 -*-
import unittest
from solutions.CHK import checkout_solution as C


class TestCheckoutRoundOne(unittest.TestCase):
    def test_checkout_abc(self):
        self.assertEqual(C.checkout('ABC'), 100)

    def test_checkout_deal_one(self):
        self.assertEqual(C.checkout('AAA'), 130)

    def test_checkout_deal_two(self):
        self.assertEqual(C.checkout('BB'), 45)

    def test_checkout_combination(self):
        """ Test should contain one 'AAA' deal, one 'BB' deal
            as well as an extra 'A', 'B', and one 'C' """
        self.assertEqual(C.checkout('AABACBAB'), 275)

    def test_checkout_d(self):
        self.assertEqual(C.checkout('DD'), 30)

    def test_checkout_illegal_int(self):
        self.assertEqual(C.checkout(12), -1)
        # with self.assertRaises(TypeError):
        #     C.checkout(12)

    def test_checkout_illegal_float(self):
        self.assertEqual(C.checkout(1.0), -1)
        # with self.assertRaises(TypeError):
        #     C.checkout(1.0)

    def test_checkout_illegal_item(self):
        self.assertEqual(C.checkout('Z'), -1)
        # with self.assertRaises(ValueError):
        #     C.checkout('Z')

    def test_checkout_lower_case(self):
        """ I am assuming that the method should be case sensitive """
        self.assertEqual(C.checkout('a'), -1)


class TestCheckoutRoundTwo(unittest.TestCase):
    def test_checkout_e(self):
        self.assertEqual(C.checkout('E'), 40)

    def test_checkout_e_deal(self):
        self.assertEqual(C.checkout('EEB'), 80)

    def test_checkout_eb_deal(self):
        """ It is important to note which is more beneficial to the customer
            is the deal using 'E' preferable to the deal on 'B's alone
            when there is an option?

            'EEBB' - either deal can apply
            'E' deal: 'EEB' = 80, 'B' = 30 -> 110
            'B' deal: 'EE' = 80, 'BB' = 45 -> 125

            Therefore 'E' deal should be favoured """
        self.assertEqual(C.checkout('EEBB'), 110)

    def test_checkout_be_deal(self):
        # Ensuring order doesn't matter...
        self.assertEqual(C.checkout('BBEE'), 110)

    def test_checkout_both_deals(self):
        self.assertEqual(C.checkout('BBBEE'), 125)

    def test_checkout_multiple_deals(self):
        self.assertEqual(C.checkout('EEEEBBBBB'), 235)

    def test_checkout_aaaaa_deal(self):
        self.assertEqual(C.checkout('AAAAA'), 200)

    def test_checkout_six_a_deals(self):
        self.assertEqual(C.checkout('AAAAAA'), 250)

    def test_checkout_six_a_deals(self):
        self.assertEqual(C.checkout('AAAAAAA'), 300)


if __name__ == '__main__':
    unittest.main()
