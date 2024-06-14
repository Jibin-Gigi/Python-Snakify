'''
A sequence consists of integer numbers and ends with the number 0. 
Determine how many elements of this sequence are greater than their neighbours above.
'''
prev = int(input())
count = 0
while prev != 0:
    element = int(input())
    if element != 0 and element > prev:
        count += 1
    prev = element    
print(count)        
        