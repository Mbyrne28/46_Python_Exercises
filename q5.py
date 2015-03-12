# Write a function translate() that will translate a text into "rovarspraket" (Swedish for "robber's language")
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

# translate("this is fun") => "tothohisos isos fofunon".

from q4 import is_a_vowel

def translate(a_string):
	translation = ""

	for a_char in a_string:
		if is_a_vowel(a_char) == True:
			translation += a_char
		else:
			translation += a_char + "o" + a_char

	return translation

print(translate("this is fun"), "tothohisos isos fofunon")
