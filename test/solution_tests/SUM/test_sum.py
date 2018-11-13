import unittest

from solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)

    """Should add exception testing later, let's get the code running"""
    def test_sum_float(self):
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
