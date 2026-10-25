import unittest

from feature_e import square


class SquareTests(unittest.TestCase):
    def test_positive_integers(self):
        for value, expected in ((1, 1), (2, 4), (7, 49), (12, 144)):
            with self.subTest(value=value):
                self.assertEqual(square(value), expected)

    def test_negative_integers(self):
        for value, expected in ((-1, 1), (-2, 4), (-7, 49), (-12, 144)):
            with self.subTest(value=value):
                self.assertEqual(square(value), expected)

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_large_integers_preserve_precision(self):
        for value in (10**100 + 1, -(10**100 + 1)):
            with self.subTest(value=value):
                self.assertEqual(square(value), 10**200 + 2 * 10**100 + 1)


if __name__ == "__main__":
    unittest.main()
