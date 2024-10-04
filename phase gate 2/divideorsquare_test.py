import unittest
import divideorsquare

class divideorsquare_test(unittest.TestCase):

	def test_that_divideorsquare_function_exists(self):

		self.assertEqual(divideorsquare.divideorsquare(11),1)


	def test_that_divideorsquare_function_returns_correct_value(self):

		self.assertEqual(divideorsquare.divideorsquare(11),1)

	
	
	def test_that_divideorsquare_function_works_with_floating_point_values(self):

		self.assertEqual(divideorsquare.divideorsquare(4.2),(4.2%5))
	
	def test_that_divideorsquare_function_Raises_error_with_String(self):

		self.assertRaises(TypeError,divideorsquare.divideorsquare, "semicolon")
		

	
	def test_that_divideorsquare_function_Raises_error_with_Negatives(self):

		self.assertRaises(ValueError,divideorsquare.divideorsquare,-2)



	
