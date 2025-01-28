'''
In mathematics, the factorial of an integer n, denoted by n! is the following product:
n!= 1 x 2 x 3...x n 
For the given integer n calculate the value n!
'''
n = int(input())
factorial = 1
for i in range(1, n+1 ):
    factorial *= i
print(factorial)    