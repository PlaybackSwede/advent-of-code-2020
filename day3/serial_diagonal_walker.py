import math

file = open('input.txt', 'r') 
lines = file.readlines()

map_matrix = [arr for arr in [line.strip() for line in lines]]

row_length = len(map_matrix)
column_length = len(map_matrix[0]) 

tree_counter = [0, 0, 0, 0, 0]
y = x = 0
series = [[1,1], [3,1], [5,1],[7,1],[1,2]]
for idx, serie in enumerate(series):
    print(idx, serie)
    y = x = 0
    while y < row_length - 1:
        for x_pos in range(serie[0]):
            if x > 0 and x%(column_length-1) == 0:
                x = 0
            else:
                x += 1

        y += serie[1]
        if y <= row_length - 1 and map_matrix[y][x] == '#':
            tree_counter[idx] += 1

print(tree_counter, math.prod(tree_counter))



