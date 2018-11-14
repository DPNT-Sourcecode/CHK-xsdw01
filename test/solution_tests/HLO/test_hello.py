# -*- coding: utf-8 -*-
import unittest

from solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_solution.hello("World"),
                         "Hello, World!")

    def test_hello_john(self):
        self.assertEqual(hello_solution.hello("John"),
                         "Hello, John!")

    def test_hello_lower_case(self):
        self.assertEqual(hello_solution.hello("john"),
                         "Hello, john!")


if __name__ == '__main__':
    unittest.main()
