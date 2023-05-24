import unittest
from findFibo import fibonacci


class test_Fibonacci(unittest.TestCase):
    def test1_fibonacci(self):
        self.assertTrue(fibonacci(10, 5))

    def test2_fibonacci(self):
        self.assertFalse(fibonacci(15, 10))


unittest.main()
