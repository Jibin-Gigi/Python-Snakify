''' Given two positive integers m and n , m lines of n elements, giving an (m × n) matrix A, 
    followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.
    Write a function swap_columns(a, i, j) and call it to exchange the columns. '''


m , n = [int(i) for i in input().split()]
matrix = [ [int(j) for j in input().split()] for i in range(m)]
i , j = [int(x) for x in input().split()]


def swap_columns(matrix,i,j):
    for row in matrix:
        row[i] , row[j] = row [j] , row[i]
    for row in matrix:
        print(' '.join(map(str,row)))    
  
swap_columns(matrix,i,j) 
    
