import unittest
import dollartonaira


class Testdollartonaira(unittest.TestCase):

	def test_that_dollar_to_naira_function_function_exist(self):
		dollartonaira.dollar_to_naira(3)

	def test_that_dollar_to_naira_function_function_returns_naira(self):
		self.assertEqual(dollartonaira.dollar_to_naira(1),1550)
		self.assertEqual(dollartonaira.dollar_to_naira(10),15500)

	def test_that_dollar_to_naira_function_function_raises_error_with_negative_numbers(self):
		self.assertRaises(ValueError,dollartonaira.dollar_to_naira,-8)

	def test_that_dollar_to_naira_function_raises_error_with_String(self):
		self.assertRaises(TypeError,dollartonaira.dollar_to_naira,"byte")
