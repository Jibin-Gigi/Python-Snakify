'''
Given a sequence of integer numbers ending with the number 0. 
Determine the length of the widest fragment where all the elements are equal to each other.
'''
element = prev = int(input())
count = 1
max_count = 1
while element != 0:
    element = int(input())
    if element == prev:
        count += 1
    else :
        max_count = max(count,max_count)
        prev = element
        count = 1
       
    
print(max_count)    
    