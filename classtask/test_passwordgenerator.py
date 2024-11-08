import unittest
import passwordgenerator


class TestCube(unittest.TestCase):

	def test_that_function_exist(self):
		passwordgenerator.generatepassword()

	def test_that_function_returns_correct_length(self):
		
		check = False

		if len(passwordgenerator.generatepassword()) >15: check=True

		self.assertTrue(check)


	def test_that_function_contains_symbols(self):

		symbol_check = passwordgenerator.generatepassword().isalnum()
		
		self.assertFalse(symbol_check)
		
	def test_that_function_contains_uppercase(self):

		upper_case_check =  passwordgenerator.generatepassword().islower()

		self.assertFalse(upper_case_check)

	def test_that_function_contains_lowercase(self):

		lower_case_check = passwordgenerator.generatepassword().isupper()

		self.assertFalse(lower_case_check)
	

	

