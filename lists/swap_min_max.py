''' Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. '''

list1 = [int(i) for i in input().split()]
min_index = list1.index(min(list1))
max_index = list1.index(max(list1))
list1[min_index] , list1[max_index] = list1[max_index] , list1[min_index]
print(' '.join([str(i) for i in list1]))
