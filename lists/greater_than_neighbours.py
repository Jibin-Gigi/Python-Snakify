''' Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.
    The first and the last items of the list shouldn't be considered because they don't have two neighbors. '''

list1 = [int(i) for i in input().split()]
count = 0
for index in range( 1,len(list1)-1 ):
    if list1[index-1] < list1[index] > list1[index+1]:
        count += 1
print(count)        
    
