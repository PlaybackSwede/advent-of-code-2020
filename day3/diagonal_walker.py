
file = open('input.txt', 'r') 
lines = file.readlines()

map_matrix = [arr for arr in [line.strip() for line in lines]]

row_length = len(map_matrix)
column_length = len(map_matrix[0]) 

tree_counter = 0
y = x = 0
while y < row_length - 1:
    for x_pos in range(3):
        if x > 0 and x%(column_length-1) == 0:
            x = 0
        else:
            x += 1

    y += 1
    if y <= row_length - 1 and map_matrix[y][x] == '#':
        tree_counter += 1

print(tree_counter)



