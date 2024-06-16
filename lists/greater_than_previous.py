''' Given a list of numbers, find and print all the elements that are greater than the previous element. '''

list1 = [int(i) for i in input().split()]
for index in range(1, len(list1)):
    if list1[index] > list1[index - 1]:
        print(list1[index])
