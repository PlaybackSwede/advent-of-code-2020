import functools

file = open('input.txt', 'r') 
lines = file.readlines()

groups = {}
i = j = 0
for line in lines:
    if line == '\n':
        i += 1
        continue
    
    if not groups.get(i):
        groups[i] = {}
    
    group_dict = groups.get(i)
    for letter in line.strip():
        if group_dict.get(j):
            group_dict[j].add(letter)
        else:
            group_dict[j] = set(letter)
    j += 1

group_sets = [list(group.values()) for group in groups.values()]
print(functools.reduce(lambda a,b : a+b, [len(set.intersection(*group)) for group in group_sets]))
    
