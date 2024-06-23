''' Given N numbers: the first number in the input is N, after that N integers are given. 
Count the number of zeros among the given integers and print it. '''


count = 0
n = int(input())
for i in range(n):
    if int(input())==0:
        count += 1
print(count)        