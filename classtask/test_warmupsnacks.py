import unittest
import warmupsnacks

class MyTestCase(unittest.TestCase):

    def test_that_function_construct_list_works(self):

        expected = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(expected,warmupsnacks.construct_list())

    def test_that_duplicate_function_works(self):
        expected = [2,4]
        self.assertEqual(expected,warmupsnacks.duplicate([1,2]))


    def test_that_remove_duplicate_function_works(self):
        expected = [3]
        self.assertEqual(expected,warmupsnacks.remove_duplicates([3,3,3,3,3]))


    def test_that_add_every_third_function_works(self):
        expected = 6
        self.assertEqual(expected,warmupsnacks.add_every_third([0,0,3,0,0,3]))

    def test_that_add_first_last_and_middle_function_works(self):
        expected = 9
        self.assertEqual(expected,warmupsnacks.add_first_last_and_middle([1,2,3,4,5]))


