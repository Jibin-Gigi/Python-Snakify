'''A timestamp is three numbers: a number of hours, minutes and seconds. 
   Given two timestamps, calculate how many seconds is between them.'''

#Using list
list1 = []
for i in range(0,2):
    list1.append(int(input())*3600)
    list1.append(int(input())*60)
    list1.append(int(input()))

seconds=abs(sum(list1[:3])-sum(list1[3:]))


print(seconds)
