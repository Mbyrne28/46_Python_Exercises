# "99 Bottles of Beer" is a traditional song in the United States and Canada.
# It is popular to sing on long trips, as it has a very repetitive format which
# is easy to memorize, and can take a long time to sing.
# The song's simple lyrics are as follows:

# 99 bottles of beer on the wall, 99 bottles of beer.

# Take one down, pass it around, 98 bottles of beer on the wall.


def sing():
	plural = "s"
	for bottle in range(99, 0, -1):
		if bottle ==1:
			plural=""
		if bottle != 99:
			print("Take one down, pass it around, %s bottle%s of beer on the wall." % (str(bottle), plural))
		print("%s bottle%s of beer on the wall, %s bottles of beer." % (str(bottle), plural, str(bottle)))

sing()