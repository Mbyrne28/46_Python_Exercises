# Represent a small bilingual lexicon as a Python dictionary in the following fashion
# {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"}
# and use it to translate your Christmas cards from English into Swedish.
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.

import unittest

def translate_cards(s):
	translation = ""
	swedish = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

	for item in s.split(" "):
		translation += " " + swedish[item]

	return translation[1:]


class test_translate_cards(unittest.TestCase):

	def test_mem(self):
		res_01 = translate_cards("happy new year")
		self.assertEqual(res_01, "gott nytt ar")

	def test_mem02(self):
		res_02 = translate_cards("merry christmas")
		self.assertEqual(res_02, "god jul")

if __name__ == '__main__':
	unittest.main()