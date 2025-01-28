'''
A cupcake costs A dollars and B cents. 
Determine, how many dollars and cents should one pay for 
N cupcakes. A program gets three numbers: A, B, N. 
It should print two numbers: total cost in dollars and cents
'''
a=int(input())
b=int(input())
cost= a + (b/100)
n=int(input())
print(int(cost*n))
print((cost*n- int(cost*n))*100)

'''
a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)
'''