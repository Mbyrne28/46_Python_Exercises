# Write a program that maps a list of words into a list of integers
# representing the lengths of the correponding words.

# words_to_int("one fish two fish red fish blue fish") => [3, 4, 3, 4, 3, 4, 4, 4]

import unittest


def words_to_int(s):
	int_list = []
	split_str = s.split(" ")

	for word in split_str:
		int_list.append(len(word))

	return int_list


class test_words_to_int(unittest.TestCase):

	def test_mem(self):
		res_01 = words_to_int("one fish two fish red fish blue fish")
		res_02 = words_to_int("Would you eat them on a train")
		self.assertEqual(res_01, [3, 4, 3, 4, 3, 4, 4, 4])
		self.assertEqual(res_02, [5, 3, 3, 4, 2, 1, 5])


if __name__ == '__main__':
	unittest.main()