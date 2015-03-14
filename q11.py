# Define a function generate_n_chars() that takes an integer n and a character c
# and returns a string, n characters long, consisting only of c:s.
# For example, generate_n_chars(5,"x") should return the string "xxxxx".

import unittest

def generate_n_chars(n, c):
	result = ""

	while n>0:
		result += c
	 	n -=1

	return result

class test_generate_n_chars(unittest.TestCase):

	def test_generate_n_chars(self):
		res_01 = generate_n_chars(5,"x")
		res_02 = generate_n_chars(6,"ab")

		self.assertEqual(res_01, "xxxxx")
		self.assertEqual(res_02, "abababababab")

if __name__ == '__main__':
	unittest.main()