import unittest
import floatchecker


class TestCube(unittest.TestCase):

	def test_thatfloat_checkerfunction_exist(self):
		floatchecker.float_checker(3,2)

	def test_thatfloat_checkerfunction_returns_correct_value(self):
		self.assertEqual(floatchecker.float_checker(2.5,6.7),2)
		self.assertEqual(floatchecker.float_checker(1.3,1),1)
		self.assertEqual(floatchecker.float_checker(1,1),0)

	def test_thatfloat_checkerfunction_raises_error_with_String(self):
		self.assertRaises(TypeError,floatchecker.float_checker,"byte")
