import unittest
import addstrings

class addstrings_test(unittest.TestCase):

	def test_that_addstrings_function_exists(self):

		self.assertEqual(addstrings.addstrings("2","3"),5)


	def test_that_addstrings_function_returns_correct_value(self):

		self.assertEqual(addstrings.addstrings("2","3"),5)

	

	def test_that_addstrings_function_returns_correct_value_with_negative_values(self):

		self.assertEqual(addstrings.addstrings("-10","10"),0)
		self.assertEqual(addstrings.addstrings("10","-10"),0)
		self.assertEqual(addstrings.addstrings("-10","-10"),-20)


	def test_that_addstrings_function_works_with_floating_point_values(self):

		self.assertEqual(addstrings.addstrings("4","0.5"),4.5)
		self.assertEqual(addstrings.addstrings("0.5","4"),4.5)


	
	def test_that_addstrings_function_Raises_error_with_String(self):

		self.assertRaises(ValueError,addstrings.addstrings("4","12v"))
		

