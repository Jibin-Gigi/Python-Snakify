''' A car can cover distance of N kilometers per day. 
    How many days will it take to cover a route of 
    length M kilometers? '''


from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
