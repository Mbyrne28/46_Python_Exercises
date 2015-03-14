# Define a function overlapping() that takes two lists and returns True
# if they have at least one member in common, False otherwise.
# You may use your is_member() function, or the in operator,
# but for the sake of the exercise, you should (also) write it using two nested for-loops.

# overlapping([23, 45, 15],[13, 14, 15, 16, 17]) => True
# overlapping(["red fish", "blue fish", "black fish"],[13, 14, 15, 16, 17]) => False
# overlapping([1, 2, 3, "green eggs"],["on a plane", "green eggs", "ham"]) => True

import unittest

def overlapping(a, b):
	result = False

	for a_element in a:
		for b_element in b:
			if a_element == b_element:
				result = True

	return result


class test_overlapping(unittest.TestCase):

	def test_mem(self):
		res_01 = overlapping([23, 45, 15],[13, 14, 15, 16, 17])
		res_02 = overlapping(["red fish", "blue fish", "black fish"],[13, 14, 15, 16, 17])
		res_03 = overlapping([1, 2, 3, "green eggs"],["on a plane", "green eggs", "ham"])
		self.assertTrue(res_01)
		self.assertFalse(res_02)
		self.assertTrue(res_03)

if __name__ == '__main__':
	unittest.main()