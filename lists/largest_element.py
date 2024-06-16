''' Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest 
    element and then the index number. If the highest element is not unique, print the index of the first instance. '''

index_of_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)

'''
list1 = [ int(i) for i in input().split()]
largest = max(list1)
if list1.count(largest) == 1 or list1 == [largest] * len(list1)  :
    print(largest,list1.index(largest))
else:
    print(list1.index(largest))

'''
    
