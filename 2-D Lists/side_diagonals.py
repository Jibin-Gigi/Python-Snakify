''' Given an integer n , create a two-dimensional array of size (n×n) 
    and populate it as follows, with spaces between each character:
        The positions on the minor diagonal (from the upper right to the lower left corner) receive 1 .
        The positions above this diagonal recieve 0 .
        The positions below the diagonal receive 2 .
    Print the elements of the resulting array. '''

n = int(input())
diagonal = [[ 0 for _ in range(n) ]for _ in range(n)]
for i in range(n):
    diagonal[i][n-i-1] = 1
    
    for j in range(n-i, n):
        diagonal[i][j] = 2
    

for row in diagonal:
    print(' '.join(map(str,row)))
