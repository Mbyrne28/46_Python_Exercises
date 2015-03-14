# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.

# histogram([4, 9, 7]) should print the following:

from q11 import generate_n_chars

def histogram(l):

	for num in l:
		print(generate_n_chars(num, "*"))


histogram([4,9,7])