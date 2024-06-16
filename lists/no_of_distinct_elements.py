''' Given a list of numbers with all of its elements sorted in ascending order, 
    determine and print the quantity of distinct elements in it. '''

counter = 1
list1 = [int(i) for i in input().split()]
for i in range(1, len(list1)):
    if list1[i] != list1[i-1]:
        counter += 1
print(counter)        
