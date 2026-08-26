import unittest
from arth import add, sub, mul


class TestArth(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50)


if __name__ == "__main__":
    unittest.main()
