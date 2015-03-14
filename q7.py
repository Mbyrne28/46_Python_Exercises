# Define a function reverse() that computes the reversal of a string.

# reverse("I am testing") => "gnitset ma I"
# reverse("Hello world") =>	"dlrow olleH"

from test_fun import *

def reverse(s):
	"""returns the reversal of a string"""
	reversed_str = ""
	for char in s:
		reversed_str = char + reversed_str

	return reversed_str

print(test_fun(reverse("I am testing"),"gnitset ma I"))
print(test_fun(reverse("Hello world"),"dlrow olleH"))