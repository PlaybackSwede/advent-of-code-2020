
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

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid' ]

# Get nbr valid passports
valid_passports = 0
for cred_dict in credentials.values():
    if set(cred_dict.keys()) == set(required_fields):
        valid_passports += 1

print(valid_passports)




