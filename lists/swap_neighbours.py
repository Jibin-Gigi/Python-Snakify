''' Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). 
    Print the resulting list. If a list has an odd number of elements, leave the last element in place. '''

list1 = [int(i) for i in input().split()]
for i in range(1,len(list1),2):
    list1[i - 1], list1[i] = list1[i], list1[i - 1]
print(' '.join([str(item) for item in list1]))
