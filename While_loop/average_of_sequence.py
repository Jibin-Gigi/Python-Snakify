'''
Determine the average of all elements of the sequence ending with the number 0.
'''
temp = 0
len = 0
element = int(input())
while element != 0:
    temp += element
    len += 1
    element = int(input())
print( temp/len )    