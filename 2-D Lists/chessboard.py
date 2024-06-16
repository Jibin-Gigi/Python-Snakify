''' Given two numbers n and m. Create a two-dimensional array of size (n x m) 
    and populate it with the characters "." and "*" in a checkerboard pattern. 
    The top left corner should have the character "." 
'''

n,m =[int(i) for i in input().split()]

check = [['.' for _ in range(m)] for _ in range(n)]
for index, row in enumerate(check):
    if index % 2 == 0:
        for i in range(1, m, 2):
            row[i] = '*'
    else:
        for i in range(0, m, 2):
            row[i] = '*'
for row in check:
    print(' '.join(row))       
    

'''
n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))
'''