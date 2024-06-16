''' Given a list of numbers, find and print the elements that appear in the list only once. 
    The elements must be printed in the order in which they occur in the original list. '''

list1 = [int(i) for i in input().split()]
for item in list1:
    if list1.count(item) == 1:
        print(item)
