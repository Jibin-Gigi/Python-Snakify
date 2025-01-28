'''
Given a sequence of non-negative integers, where each number is written in a separate line. 
Determine the length of the sequence, where the sequence ends when the integer is equal to 0. 
Print the length of the sequence (not counting the integer 0). 
The numbers following the number 0 should be omitted.
'''

length = 0
while int(input()) != 0:
    length += 1
print(length)