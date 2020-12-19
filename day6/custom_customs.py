import functools

file = open('input.txt', 'r') 
lines = file.readlines()

groups = {}
i = 0
for line in lines:
    if line == '\n':
        i += 1
        continue
    
    for letter in line.strip():
        if groups.get(i):
            groups[i].add(letter)
        else:
            groups[i] = set(letter)

print(functools.reduce(lambda a,b : a+b, [len(group) for group in groups.values()]))
    
