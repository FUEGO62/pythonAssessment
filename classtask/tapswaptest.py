import unittest
import tapswap


class TestTapSwap(unittest.TestCase):

	def test_that_my_discount_function_returns_correct_value(self):

		numbers = [1,2,3,4,5,6]
		result = [2,1,4,3,6,5]

		self.assertEqual(tapswap.swap(numbers),result)

