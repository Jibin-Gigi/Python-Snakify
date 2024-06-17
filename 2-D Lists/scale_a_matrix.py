''' Given two positive integers m and n, m lines of n elements, giving an (m × n) matrix A, 
    followed by one integer c , multiply every entry of the matrix by c and print the result. '''

m , n = [int(i) for i in input().split()]
A = [ [int(j) for j in input().split()] for i in range(m) ]

c = int(input())

for row in A:
    print(' '.join(map(str,row[i]*c for i in range(n) )))


'''
m, n = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
c = int(input())

for i in range(m):
    for j in range(n):
        A[i][j] *= c

print('\n'.join([' '.join([str(k) for k in row]) for row in A]))
'''
