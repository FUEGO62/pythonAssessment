import unittest
import discount


class TestCube(unittest.TestCase):

	def test_that_my_discount_function_exist(self):
		discount.my_discount(3,2)

	def test_that_my_discount_function_returns_correct_value(self):
		self.assertEqual(discount.my_discount(60,50),30)
		self.assertEqual(discount.my_discount(200,10),180)
		self.assertEqual(discount.my_discount(100,50),50)

	def test_that_my_discount_function_raises_error_with_String(self):
		self.assertRaises(TypeError,discount.my_discount,"byte")


	def test_that_my_discount_function_raises_error_with_negative_values(self):
		self.assertRaises(TypeError,discount.my_discount,(-3,-4))
