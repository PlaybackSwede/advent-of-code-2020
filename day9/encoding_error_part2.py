import itertools

file = open('input.txt', 'r') 
lines = file.readlines()

nbrs = [int(nbr.strip()) for nbr in lines]

preamble_size = 25
i = preamble_size
invalid_nbr = 0
for nbr in nbrs[preamble_size:]:
    preamble = nbrs[i - preamble_size:i]
    for comb in list(itertools.combinations(preamble, 2)):
        if sum(comb) == nbr:
            break
    else:
        #Found first invalid nbr
        invalid_nbr = nbr
        break
    i += 1

i = 0
for i in range(len(nbrs)):
    result = 0
    for j in range(1, len(nbrs)):
        seq = nbrs[i:j]
        calc_sum = sum(seq)
        if calc_sum > invalid_nbr:
            break
        if calc_sum == invalid_nbr:
            result = min(seq) + max(seq)
            print(result)
            break
    if result > 0:
        break

    








    

    
