''' Given a sequence of integers that end with a 0. Print the sequence in reverse order.
    Don't use lists or other data structures. Use the force of recursion instead.'''

def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()