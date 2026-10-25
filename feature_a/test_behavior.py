import unittest

from feature_a import add


class AdditionBehaviorTests(unittest.TestCase):
    def test_signed_integer_addition(self):
        cases = [
            (2, 3, 5),
            (-2, -3, -5),
            (-7, 4, -3),
            (7, -4, 3),
            (-9, 9, 0),
            (0, 0, 0),
            (0, 8, 8),
            (8, 0, 8),
            (0, -8, -8),
            (-8, 0, -8),
        ]
        for left, right, expected in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(add(left, right), expected)

    def test_arbitrary_precision_integer_addition(self):
        large = 10 ** 100
        self.assertEqual(add(large, 1), large + 1)
        self.assertEqual(add(-large, -1), -large - 1)
        self.assertEqual(add(large, -large), 0)


if __name__ == "__main__":
    unittest.main()
