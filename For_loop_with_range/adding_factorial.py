'''
Given an integer n, print the sum 1!+2!+3!+...+n!
This problem has a solution with only one loop, so try to discover it.
'''

result = 0
fact = 1
n = int(input())
for i in range(1, n+1):
    fact *= i
    result += fact
print(result)    