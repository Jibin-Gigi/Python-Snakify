'''
A sequence consists of integer numbers and ends with the number 0. 
Determine how many elements of this sequence are equal to its largest element.
'''
max = 0
count = 0
element = int(input())
while element!= 0:
    if element > max:
        max = element
        count = 1
    elif element == max:
        count += 1
    element = int(input())
print(count)    