'''
Determine the number of even elements in the sequence ending with the number 0.
'''
count = 0
element = int(input())
while element != 0:
    if element % 2 == 0:
        count += 1
    element = int(input())    
print(count)    