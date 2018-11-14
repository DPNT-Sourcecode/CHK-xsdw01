# -*- coding: utf-8 -*-
import unittest

from solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello("Any string"),
                         "Hello, World!")


if __name__ == '__main__':
    unittest.main()
