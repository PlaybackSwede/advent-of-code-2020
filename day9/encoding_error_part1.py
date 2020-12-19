import itertools

file = open('input.txt', 'r') 
lines = file.readlines()

nbrs = [int(nbr.strip()) for nbr in lines]

preamble_size = 25
i = preamble_size
for nbr in nbrs[preamble_size:]:
    preamble = nbrs[i - preamble_size:i]
    for comb in list(itertools.combinations(preamble, 2)):
        if sum(comb) == nbr:
            break
    else:
        #Found first invalid nbr
        print(nbr)
        break

    i += 1
    








    

    
