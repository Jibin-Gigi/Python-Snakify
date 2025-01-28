'''
The sequence consists of distinct positive integer numbers and ends 
with the number 0. Determine the value of the second largest element in this 
sequence. It is guaranteed that the sequence has at least two elements.
'''
largest = 0
second = 0
element = int(input())
while element != 0:
    if element > largest:
        second = largest
        largest = element
    elif element > second:
        second = element
    element = int(input())    
print(second)        
        
        