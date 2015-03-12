# Write a function that takes a character (i.e. a string of length 1) 
# and returns True if it is a vowel, False otherwise.

# is_a_vowel("i") => True
# is_a_vowel("b") => False
# is_a_vowel("2") => False

def is_a_vowel(a_char):
	vowels = ["a", "e", "i", "o", "u", "y"]
	vowel_check = False

	for vowel in vowels:
		if vowel == a_char:
			vowel_check = True

	return vowel_check


print(is_a_vowel("i"),True)
print(is_a_vowel("b"), False)
print(is_a_vowel("2"), False)