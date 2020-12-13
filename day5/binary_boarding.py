import math

def get_row_or_col(text, lb, ub, lower_half_char):
    result = 0
    for char in text:
        distance = (ub - lb)/2
        if char == lower_half_char:
            #lower half
            if distance < 1:
                #Take lb seat
                result = lb
                break
            ub = math.floor(ub - distance)
        else:
            #upper half
            if distance < 1:
                #Take lb seat
                result = ub
                break
            lb = math.ceil(lb + distance)
    return result

file = open('input.txt', 'r') 
lines = file.readlines()

boarding_passes = [line.strip() for line in lines]

rows = []
columns = []
for boarding_pass in boarding_passes:
    row_text = boarding_pass[:7]
    rows.append(get_row_or_col(row_text, 0, 127, 'F'))
    col_text = boarding_pass[-3:]
    columns.append(get_row_or_col(col_text, 0, 7, 'L'))

highest_seat_id = max([row*8 + col for (row, col) in set(zip(rows, columns))])

print(highest_seat_id)



    




