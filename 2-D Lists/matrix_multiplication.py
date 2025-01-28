''' Given three positive integers m , n and r , m lines of n elements, giving an (m × n) matrix A, and n lines of r elements, 
    giving an (n × r) matrix B, form the product matrix AB, which is the m×r matrix whose (i,k) entry is the sum
              A[i][1]∗B[1][k]+⋯+A[i][n]∗B[n][k]
    and print the result. ''' 

m , n , r = [int(i) for i in input().split()]
A = [ [int(j) for j in input().split()] for i in range(m) ]
B = [ [int(j) for j in input().split()] for i in range(n) ]

result=[ [0 for k in range(r)] for i in range(m) ]

temp = 0
for i in range(m):
    for j in range(n):
        for k in range(r):
            result[i][k] +=  A[i][j]*B[j][k]


for row in result:
    print(' '.join(map(str, row)))
