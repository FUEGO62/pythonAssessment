import unittest
import discount


class TestCube(unittest.TestCase):

	def test_that_my_discount_function_exist(self):
		discount.my_discount(3,2)

	def test_that_my_discount_function_returns_correct_value(self):
		self.assertEqual(discount.my_discount(6),30)

	def test_that_my_discount_function_raises_error_with_String(self):
		self.assertRaises(TypeError,discount.my_discount,"byte")


