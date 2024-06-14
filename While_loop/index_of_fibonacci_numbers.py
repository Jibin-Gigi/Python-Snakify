'''
The Fibonacci sequence is defined as follows:
    ϕ0=0, ϕ1=1, ϕn = ϕn-1 + ϕn-2.
Given an integer a, determine its index among the Fibonacci numbers, that is,
print the number n such that 
    ϕn=a
If a is not a Fibonacci number, print -1.
 '''
a = int(input())
index = 0
result = 0
i = 1
n1 = 1
while result < a :
    temp = result
    result = result + n1
    n1 = temp
    index += 1
if a == result:    
    print(index) 
else:
    print(-1)

'''
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)
'''    