# Write a function filter_long_words() that takes a list of words
# and an integer n and returns the list of words that are longer than n

import unittest

def filter_long_words(l, n):
	result = []

	for item in l:
		if len(item) > n:
			result.append(item)

	return result


class test_filter_long_words(unittest.TestCase):

	def test_mem(self):
		res_01 = filter_long_words(["Would", "you", "eat", "them", "on", "a", "train"], 4)
		self.assertEqual(res_01, ["Would", "train"])

if __name__ == '__main__':
	unittest.main()