import unittest
import futurevalue


class TestCube(unittest.TestCase):

	def test_that_get_future_value_function_exist(self):
		futurevalue.get_future_value(3,3,2)

	def test_that_get_future_value_function_returns_cube(self):
		self.assertEqual(futurevalue.get_future_value(1,0,1),1)
	
	def test_that_get_future_value_function_raises_error_with_negative_numbers(self):
		self.assertRaises(ValueError,futurevalue.get_future_value,-8,2,4)

	def test_that_get_future_value_function_raises_error_with_floating_point_numbers(self):
		self.assertRaises(ValueError,futurevalue.get_future_value,33,42,1.3)
	

	def test_that_get_future_value_function_raises_error_with_String(self):
		self.assertRaises(TypeError,futurevalue.get_future_value,"byte")
