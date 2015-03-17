# Define a simple "spelling correction" function correct() that takes a string
# and sees to it that
# 1) two or more occurrences of the space character is compressed into one
# 2) inserts an extra space after a period if the period is directly followed by a letter.

# correct("This   is  very funny  and    cool.Indeed!") => "This is very funny and cool. Indeed!"

import unittest
import re

def correct(s):
	corrected=""
	result=""
	p = re.compile('(\s)+')
	q = re.compile('\.(\S+)')

	corrected = p.sub(" ", s)

	corrected = q.split(corrected)

	for i in range(1, len(corrected)):
		result += corrected[i-1] + ". "

	result = result[:-2]


	return result
correct("This   is  very funny  and    cool.Indeed!")
class test_correct(unittest.TestCase):

	def test_mem(self):
		res_01 = correct("This   is  very funny  and    cool.Indeed!")
		res_02 = correct("This   is  very.funny.and    cool indeed!")
		self.assertEqual(res_01, "This is very funny and cool. Indeed!")
		self.assertEqual(res_02, "This is very. funny. and cool indeed!")

if __name__ == '__main__':
	unittest.main()