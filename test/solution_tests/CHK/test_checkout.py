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

    # def test_checkout_illegal_item(self):
    #     self.assertEqual(C.checkout('Z'), -1)

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


class TestCheckoutRoundThree(unittest.TestCase):
    def test_checkout_f(self):
        self.assertEqual(C.checkout('F'), 10)

    def test_checkout_f_not_enough(self):
        self.assertEqual(C.checkout('FF'), 20)

    def test_checkout_f_deal(self):
        # Is this not the same as a discount on 3 F's?
        self.assertEqual(C.checkout('FFF'), 20)

    def test_checkout_four_fs(self):
        self.assertEqual(C.checkout('FFFF'), 30)

    def test_checkout_five_fs(self):
        self.assertEqual(C.checkout('FFFFF'), 40)

    def test_checkout_six_fs(self):
        self.assertEqual(C.checkout('FFFFFF'), 40)


class TestCheckoutRoundFour(unittest.TestCase):
    def test_checkout_5h(self):
        self.assertEqual(C.checkout('HHHHH'), 45)

    def test_checkout_10h(self):
        self.assertEqual(C.checkout('HHHHHHHHHH'), 80)

    def test_checkout_15h(self):
        self.assertEqual(C.checkout('HHHHHHHHHHHHHHH'), 125)

    def test_checkout_2k(self):
        self.assertEqual(C.checkout('KK'), 150)

    def test_checkout_3n1m(self):
        self.assertEqual(C.checkout('NNNM'), 120)

    def test_checkout_5p(self):
        self.assertEqual(C.checkout('PPPPP'), 200)

    def test_checkout_3q(self):
        self.assertEqual(C.checkout('QQQ'), 80)

    def test_checkout_3r1q(self):
        self.assertEqual(C.checkout('RRRQ'), 150)

    def test_checkout_4u(self):
        self.assertEqual(C.checkout('UUUU'), 120)

    def test_checkout_2v(self):
        self.assertEqual(C.checkout('VV'), 90)

    def test_checkout_3v(self):
        self.assertEqual(C.checkout('VVV'), 130)

    def test_checkout_rq_deals(self):
        """ R and Q deals at risk of clashing

            'QQQRRR' - which deal is better?
            'QQQ'=80, 'RRR'=150 -> 230
            'QQ'=60, 'QRRR'=150 -> 210
            Second deal should be prioritised """
        self.assertEqual(C.checkout('QQQRRR'), 210)


if __name__ == '__main__':
    unittest.main()
