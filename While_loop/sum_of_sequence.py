'''
Determine the sum of all elements in the sequence, ending with the number 0.
'''
result = 0
element = int(input())
while element != 0:
    result += element
    element = int(input())
print(result)