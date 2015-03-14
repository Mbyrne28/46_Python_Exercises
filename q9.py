# Write a function is_member() that takes a value (i.e. a number, string, etc) x
# and a list of values a, and returns True if x is a member of a, False otherwise.

# is_member(42, [1, 33, 21, 42, 99]) => True
# is_member(73, [1, 33, 21, 42, 99]) => False
# is_member("red fish", ["one fish", "two fish", "red fish", "blue fish"]) => True
# is_member([1, 2, 42], [22, [1,3], [1, 2, 42]]) => True

from test_fun import *
import unittest

def is_member(x, a):
	result = False

	for element in a:
		if element == x:
			result = True

	return result


print(test_fun(is_member(42, [1, 33, 21, 42, 99]), True))
print(test_fun(is_member(73, [1, 33, 21, 42, 99]), False))
print(test_fun(is_member("red fish", ["one fish", "two fish", "red fish", "blue fish"]), True))
print(test_fun(is_member([1, 2, 42], [22, [1,3], [1, 2, 42]]), True))

class test_is_member(unittest.TestCase):

	def test_mem(self):
		res = is_member(42, [1, 33, 21, 42, 99])
		self.assertEqual(res, True)

if __name__ == '__main__':
	unittest.main()

print(self.assertEqual(4, 23))