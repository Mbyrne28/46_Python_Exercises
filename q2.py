# Define a function max_of_three() 
# that takes three numbers as arguments and returns the largest of them.


# test max_of_three(3,4,2) => 4
# test max_of_three(2,4,3) => 4
# test max_of_three(45,500,-4) => 500
# test max_of_three (-300, -400, -600) => -300

def max_of_three(a,b,c):
	largest = 0

	largest = max(max(a,b),c)

	return largest

print(max_of_three(3,4,2), 4)
print(max_of_three(2,4,3), 4)
print(max_of_three(45,500,-4), 500)
print(max_of_three(-300, -400, -600), -300)