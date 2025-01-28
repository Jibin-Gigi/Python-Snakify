''' Given a positive real number a and a non-negative integer n. Calculate a^n 
    without using loops, ** operator or the built in function math.pow(). 
    Instead, use recursion and the relation a^n= a x a^n 
    Print the result.
    Form the function power(a, n). '''

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n-1)

a = float(input())
n = float(input())

print(power(a, n))
   


