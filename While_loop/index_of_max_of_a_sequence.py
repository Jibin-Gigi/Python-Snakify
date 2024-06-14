'''
A sequence consists of integer numbers and ends with the number 0. 
Determine the index of the largest element of the sequence. 
If the highest element is not unique, print the index of the first of them.
'''
element = int(input())
list1 = []
while element != 0:
    list1.append(element)
    element = int(input())
print(list1.index(max(list1))+1)    

'''
max = 0
len = 1
index = 0
element = int(input())
while element != 0:
    if max < element :
        max = element
        index = len
    len += 1    
    element = int(input())
print(index)    
'''