import math

def get_row_or_col(text, lb, ub, lower_half_char):
    result = 0
    for char in text:
        distance = (ub - lb)/2
        if char == lower_half_char:
            #lower half
            if distance < 1:
                #Take lowerbound
                result = lb
                break
            ub = math.floor(ub - distance)
        else:
            #upper half
            if distance < 1:
                #Take upperbound 
                result = ub
                break
            lb = math.ceil(lb + distance)
    return result

file = open('input2.txt', 'r') 
lines = file.readlines()

boarding_passes = [line.strip() for line in lines]

rows = []
columns = []
for boarding_pass in boarding_passes:
    row_text = boarding_pass[:7]
    rows.append(get_row_or_col(row_text, 0, 127, 'F'))
    col_text = boarding_pass[-3:]
    columns.append(get_row_or_col(col_text, 0, 7, 'L'))

seat_ids = sorted([row*8 + col for (row, col) in set(zip(rows, columns))])

i = 0
while i + 3 != len(seat_ids):
    [left, middle, right] = seat_ids[i:i+3]
    if left + 1 != middle:
        print(left+1)
        break
    elif right - 1 != middle:
        print(right-1)
        break
    i += 1





    




