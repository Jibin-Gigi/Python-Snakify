''' Given an odd number integer n, produce a two-dimensional array of size (n x n). 
    Fill each element with a single character string of "." . Then fill the middle row, 
    the middle column and the diagnals with the single character string of "*" (an image of a snow flake). 
    Print the array elements in (n x n) rows and columns and separate the characters with a single space. '''

n = int(input())
snowflakes = []
for row in range(n):
    snowflakes.append(['.' for row in range(n)])
for row in range(n):
    for col in range(n):
        snowflakes[n//2][col] ='*'
        snowflakes[row][n//2] ='*'
        if row == col or row+col==n-1:
            snowflakes[row][col]='*'

for row in range(n):
    print(' '.join(snowflakes[row]))


''' 
n = int(input())
snowflakes = [['.' for _ in range(n)] for _ in range(n)]

# Fill the middle row and column
for i in range(n):
    snowflakes[n//2][i] = '*'
    snowflakes[i][n//2] = '*'

# Fill the main and secondary diagonals
for i in range(n):
    snowflakes[i][i] = '*'
    snowflakes[i][n - 1 - i] = '*'

# Print the pattern
for row in snowflakes:
    print(' '.join(row))

'''
