# Define a function max() that takes two numbers as arguments and returns
# the largest of them. Use the if-then-else construct available in Python.
# (It is true that Python has the max() function built in,

# test max(3,4) => 4
# test max(4,3) => 4
# test max(300,-4) => 300
# test max (-300, -400) => -300

def max(a,b):
    largest=0

    if a > b:
        largest = a
    else:
        largest = b

    return largest

print(max(3,4),4)
print(max(4,3),4)
print(max(300,-4),300)
print(max(-300, -400),-300)
