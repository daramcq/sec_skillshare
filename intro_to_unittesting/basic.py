import unittest

def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_1_plus_1(self):
        self.assertEqual(2, add(1,1))

    def test_4_plus_4(self):
        self.assertEqual(8, add(4, 4))


if __name__ == '__main__':
    unittest.main()
