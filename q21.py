# Write a function char_freq() that takes a string and builds a frequency
# listing of the characters contained in it.
# Represent the frequency listing as a Python dictionary.

# char_freq("abbabcbdbabdbdbabababcbcbab")

import unittest

def char_freq(s):
	freq = {}

	for item in s:
		if item in freq:
			freq[item] +=1
		else:
			freq[item] =1

	return freq

class test_char_freq(unittest.TestCase):

	def test_mem(self):
		res_01 = char_freq("abbabcbdbabdbdbabababcbcbab")
		self.assertEqual(res_01, {"a":7, "b":14, "c":3, "d":3})

if __name__ == '__main__':
	unittest.main()