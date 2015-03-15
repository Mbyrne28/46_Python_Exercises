# Write a version of a palindrome recognizer that also accepts phrase palindromes
# such as "Go hang a salami I'm a lasagna hog."

import unittest
import re
from q8 import is_palindrome

def palindrome_phrase(s):
	result = False
	only_chars = ""

	for item in s:
		if (re.match("\w",item)!=None):
			only_chars += item.lower()

	if is_palindrome(only_chars):
		result = True

	return result


class test_palindrome_phrase(unittest.TestCase):

	def test_mem(self):
		res_01 = palindrome_phrase("Go hang a salami I'm a lasagna hog.")
		self.assertTrue(res_01)

if __name__ == '__main__':
	unittest.main()