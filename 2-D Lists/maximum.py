''' Given two integers representing the rows and columns (m x n), and subsequent m rows of n
    elements, find the index position of the maximum element and print two numbers representing the index (i x j) 
    or the row number and the column number. If there exist multiple such elements in different rows, 
    print the one with smaller row number. If there multiple such elements occur on the same row, 
    output the smallest column number. '''


m, n = [int(i) for i in input().split()]

list1 = []
for i in range(m):
    list1.append([int(i) for i in input().split()]) 

max_index = [0, 0]
max_value = -float('inf')  # Initialize to negative infinity
for index, row in enumerate(list1):
    row_max = max(row)
    if row_max > max_value:
        max_value = row_max
        max_index = [index, row.index(row_max)]

print(' '.join(map(str, max_index)))


'''
# Read the dimensions of the grid
rows, cols = [int(i) for i in input().split()]

# Initialize the grid with input values
grid = [[int(j) for j in input().split()] for _ in range(rows)]

# Initialize variables to track the maximum value and its position
max_value = grid[0][0]
max_position = (0, 0)

# Iterate over each element in the grid to find the maximum value and its position
for row_index in range(rows):
    for col_index in range(cols):
        if grid[row_index][col_index] > max_value:
            max_value = grid[row_index][col_index]
            max_position = (row_index, col_index)

# Print the position of the maximum value
print(max_position[0],max_position[1])


'''