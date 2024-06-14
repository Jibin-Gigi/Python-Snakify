''' Given two cells of a chessboard. If they are painted in one color, 
    print the word YES, and if in a different color - NO.
    The program receives the input of four numbers from 1 to 8, 
    each specifying the column and row number, first two - for the first cell, 
    and then the last two - for the second cell '''

row1 = int(input())
column1 = int(input())
row2 = int(input())
column2 = int(input())

if (row1 + column1 + row2 + column2) % 2 == 0:
    print('YES')
else:
    print('NO')
