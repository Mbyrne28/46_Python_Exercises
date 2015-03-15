# The function max() from exercise 1) and the function max_of_three() from exercise 2)
# will only work for two and three numbers, respectively. But suppose we have a much
# larger number of numbers, or suppose we cannot tell in advance how many they are?
# Write a function max_in_list() that takes a list of numbers and returns the largest one.

import unittest

def max_in_list(l):
	largest = l[0]

	for item in l:
		if item > largest:
			largest = item

	return largest

class test_max_in_list(unittest.TestCase):

	def test_mem(self):
		res_01 = max_in_list([1, 33, 21, 42, 99])
		res_02 = max_in_list([1001, 33, 21, 42, 99])
		res_03 = max_in_list([1, 3399, 21, 42, 99])
		self.assertEqual(res_01, 99)
		self.assertEqual(res_02, 1001)
		self.assertEqual(res_03, 3399)

if __name__ == '__main__':
	unittest.main()