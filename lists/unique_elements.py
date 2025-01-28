''' Given a list of numbers, find and print the elements that appear in the list only once. 
    The elements must be printed in the order in which they occur in the original list. '''

list1 = [int(i) for i in input().split()]
for item in list1:
    if list1.count(item) == 1:
        print(item)


'''OR

a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')

'''
        
