'''
For a given integer N, find the greatest integer x where 2^x
is less than or equal to N. Print the exponent value and the result of the expression 2^x
'''

n = int(input())
result = 1
x = 0
while result <= n:
    result *= 2
    x += 1
print(x-1,result//2)    

