import unittest
from findMax import Maximum


class MaxTest(unittest.TestCase):
    def test_Max_manfiy(self):
        numberone = Maximum(-9, -43, 0)
        self.assertEqual(numberone, 0)

    def test_Max_musbat(self):
        numbertwo = Maximum(123, -7565, 231343)
        self.assertEqual(numbertwo, 231343)

    def test_Max_double(self):
        numberthree = Maximum(1234, 34, 231343)
        self.assertEqual(numberthree, 34)


unittest.main()
