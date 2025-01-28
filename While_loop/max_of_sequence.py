'''
A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence.
'''

max = 0
element = int(input())
while element != 0:
    if max < element :
        max = element
    element = int(input())
print(max)    

