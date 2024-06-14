'''
Given an integer not less than 2. Print its smallest integer divisor greater than 1.
'''

n = int(input())
i = 2
while i <= n:
    if n % i == 0:
        print(i)
        break
    i += 1
