''' Given a list of numbers, find and print the first adjacent elements which have the same sign. 
    If there is no such pair, leave the output blank. '''

list1 = [int(i) for i in input().split()]
for i in range(1,len(list1)):
    if list1[i - 1] * list1[i] > 0:
        print(list1[i-1],list1[i])
        break
