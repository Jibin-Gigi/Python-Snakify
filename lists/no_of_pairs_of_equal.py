''' Given a list of numbers, count how many element pairs have the same value (are equal). 
    Any two elements that are equal to each other should be counted exactly once. '''

list1 = [int(i) for i in input().split()]
counter = 0
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] == list1[j]:
            counter += 1
print(counter)            
