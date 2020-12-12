import regex as re

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
        
def is_valid_hcl_format(color_str):
    for char in color_str:
        if char not in char_range('a', 'f') and char not in char_range('0', '9'):
            return False
    return True

def is_valid_pid_format(color_str):
    for char in color_str:
        if char not in char_range('0', '9'):
            return False
    return True
    

file = open('input.txt', 'r') 
lines = file.readlines()

credentials = [arr for arr in [line for line in lines]]

credentials = {}
idx = 0
for line in lines:
    if line != '\n':
        for cred_pair in line.strip().split(' '):
            [field, value] = cred_pair.split(':')
            if field == 'cid':
                continue
            if credentials.get(idx):
                credentials.get(idx)[field] = value
            else:
                credentials[idx] = {field : value}
    else:
        idx += 1

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid']

# Get nbr valid passports
valid_passports = 0
for cred_dict in credentials.values():
    if set(cred_dict.keys()) == set(required_fields):
        valid = True
        for field, val in cred_dict.items():
            if field == 'byr':
                if len(val) != 4 or not int(val) >= 1920 or not int(val) <= 2002:
                    valid = False
                    break
            elif field == 'iyr':
                if len(val) != 4 or not int(val) >= 2010 or not int(val) <= 2020:
                    valid = False
                    break
            elif field == 'eyr':
                if len(val) != 4 or not int(val) >= 2020 or not int(val) <= 2030:
                    valid = False
                    break
            elif field == 'hgt':
                metric = val[-2:]
                if metric in ['cm', 'in']:
                    nbr = int(val[:-2])
                    if metric == 'cm' and (not nbr >= 150 or not nbr <= 193):
                        valid = False
                        break
                    elif metric == 'in' and (not nbr >= 59 or not nbr <= 76):
                        valid = False
                        break
                else:
                    valid = False
                    break
            elif field == 'hcl':
                color_str = val[1:]
                if val[0] != '#' or len(color_str) != 6 or not is_valid_hcl_format(color_str):
                    valid = False
                    break
            elif field == 'ecl':
                if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    valid = False
                    break
            elif field == 'pid':
                if len(val) != 9 or not is_valid_pid_format(val):
                    valid = False
                    break
        if valid:  
            valid_passports += 1

print(valid_passports)




