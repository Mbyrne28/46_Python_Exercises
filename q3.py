# Define a function that computes the length of a given list or string. 
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

#	string_length("abcdefg") => 7
#	string_length("ab de") => 5
#	string_length("ab de g") => 7

def string_length(my_str):
	length = 0
	for char in my_str:
		length +=1

	return length


print(string_length("abcdefg"),7)
print(string_length("ab de"), 5)
print(string_length("ab de g"), 7)