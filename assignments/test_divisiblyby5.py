import unittest
import divisibleby5


class Testdivisibleby5(unittest.TestCase):

	def test_that_divide_or_square_exist(self):
		divisibleby5.divide_or_square(3)

	def test_that_divide_or_square_returns_correct_value(self):
		self.assertEqual(divisibleby5.divide_or_square(100),10)
		self.assertEqual(divisibleby5.divide_or_square(6),1)

	def test_that_divide_or_square_function_raises_error_with_negative_numbers(self):
		self.assertRaises(ValueError,divisibleby5.divide_or_square,-8)

	def test_divide_or_square_function_raises_error_with_String(self):
		self.assertRaises(TypeError,divisibleby5.divide_or_square,"byte")

def test_that_divide_or_square_function_raises_error_with_floating_point_numbers(self):
		self.assertRaises(ValueError,divisibleby5.divide_or_square,22.3)
