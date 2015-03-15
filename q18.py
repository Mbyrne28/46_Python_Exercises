# A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog.
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

import unittest

def pangram(s):
	result = False
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
	"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	s = s.lower()

	for item in s:
		if item in alphabet:
			alphabet.remove(item)
	if len(alphabet)==0:
		result = True

	return result

class test_pangram(unittest.TestCase):

	def test_mem(self):
		res_01 = pangram("The quick brown fox jumps over the lazy dog")
		self.assertTrue(res_01)

if __name__ == '__main__':
	unittest.main()