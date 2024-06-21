''' The Fibonacci sequence is defined as follows:
        ϕ0=0, ϕ1=1, ϕn=ϕn-1 + ϕn-2.
    Given a non-negative integer n, print the nth Fibonacci number ϕn '''


n = int(input())
result = 0
i = 1
n1 = 1
while i <= n:
    temp = result
    result = result + n1
    n1 = temp
    i += 1
print(result)    
    
'''
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)
'''   
    
    
    
    
    
