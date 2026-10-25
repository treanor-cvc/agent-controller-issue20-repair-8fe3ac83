import unittest

from feature_f import absolute


class AbsoluteTests(unittest.TestCase):
    def test_positive_integers_keep_their_magnitude(self):
        for value in (1, 7, 123456789):
            with self.subTest(value=value):
                self.assertEqual(absolute(value), value)

    def test_negative_integers_return_positive_magnitude(self):
        for value, expected in ((-1, 1), (-7, 7), (-123456789, 123456789)):
            with self.subTest(value=value):
                self.assertEqual(absolute(value), expected)

    def test_zero_remains_zero(self):
        self.assertEqual(absolute(0), 0)

    def test_arbitrary_precision_integers(self):
        magnitude = 10 ** 100
        self.assertEqual(absolute(magnitude), magnitude)
        self.assertEqual(absolute(-magnitude), magnitude)


if __name__ == "__main__":
    unittest.main()
