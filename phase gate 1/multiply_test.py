import unittest
import multiply

class test_multiply(unittest.TestCase):

	def test_that_multiply_function_exists(self):

		self.assertEqual(multiply.multiply(5,6),30)


	def test_that_multiply_function_returns_correct_value(self):

		self.assertEqual(multiply.multiply(10,10),100)
	

	def test_that_multiply_function_returns_correct_value_with_negative_values(self):

		self.assertEqual(multiply.multiply(-10,10),-100)
		self.assertEqual(multiply.multiply(10,-10),-100)
		self.assertEqual(multiply.multiply(-10,-10),100)


	def test_that_multiply_function_works_with_floating_point_values(self):

		self.assertEqual(multiply.multiply(4,0.5),2)
		self.assertEqual(multiply.multiply(0.5,4),2)



	def test_that_multiply_function_Raises_error_with_String(self):

		self.assertRaises(TypeError,multiply.multiply(4,"string"))
		self.assertRaises(TypeError,multiply.multiply("sring","string"))
		self.assertRaises(TypeError,multiply.multiply("string",4))


