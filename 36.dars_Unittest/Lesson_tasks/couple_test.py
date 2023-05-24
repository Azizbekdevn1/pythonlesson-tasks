import unittest
from couple import coupleIs

nums = [2, 3, 4, 5, 5, 678, 64, 43, 76, 98, -43]
couple = [3, 4, 678, 64, 76, 98]


class test_couplenums(unittest.TestCase):
    def test_couple(self):
        numbers = coupleIs(nums)
        for i in range(0, len(couple)):
            self.assertEqual(numbers[i], couple[i])


unittest.main()
