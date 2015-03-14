# Define a function is_palindrome() that recognizes palindromes
# (i.e. words that look the same written backwards).


# is_palindrome("radar") => True
# is_palindrome("matthew") => False
# is_palindrome("abba") => True



from test_fun import *
from q7 import *

def is_palindrome(s):
	result = False

	if reverse(s) == s:
		result = True

	return result

print(test_fun(is_palindrome("radar"), True))
print(test_fun(is_palindrome("matthew"), False))
print(test_fun(is_palindrome("abba"), True))