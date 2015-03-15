# Write a function find_longest_word() that takes a list of words and
# returns the length of the longest one.

import unittest
from q13 import max_in_list
from q14 import words_to_int

def find_longest_word(s):

	return max_in_list(words_to_int(s))

class test_find_longest_word(unittest.TestCase):

	def test_mem(self):
		res_01 = find_longest_word("Would you eat them on a train")
		res_02 = find_longest_word("Occupy beard sustainable hoodie tousled Vice asymmetrical")
		self.assertEqual(res_01, 5)
		self.assertEqual(res_02, 12)

if __name__ == '__main__':
	unittest.main()