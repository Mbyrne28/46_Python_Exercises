# The function max() from exercise 1) and the function max_of_three() from exercise 2)
# will only work for two and three numbers, respectively. But suppose we have a much
# larger number of numbers, or suppose we cannot tell in advance how many they are?
# Write a function max_in_list() that takes a list of numbers and returns the largest one.

import unittest

def max_in_list(l):

	pass

class test_max_in_list(unittest.TestCase):

	def test_mem(self):
		res_01 = max_in_list([1, 33, 21, 42, 99])
		self.assertEqual(res_01, 99)

if __name__ == '__main__':
	unittest.main()