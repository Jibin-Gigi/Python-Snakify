''' Given a list of numbers, find and print all elements that are an even number. 
    In this case use a for-loop that iterates over the list, and not over its indices! '''

list1 = input().split()
for item in list1:
    if int(item) % 2 == 0:
        print(item)
