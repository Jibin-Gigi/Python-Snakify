''' Given a positive real number a and integer n.  Compute a^n .  Write a function 
    power(a, n) to calculate the results using the function and print the result of the expression. '''

def power(a,n):
    return a**n

a = float(input())
n = float(input())
print(power(a,n))