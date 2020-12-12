

file = open('input.txt', 'r') 
lines = file.readlines()


position_count_pairs = [
        [int(arr[0].split('-')[0]), 
        int(arr[0].split('-')[1]), 
        arr[1][0],
        arr[2]] 
        for arr in [line.strip().split(' ') for line in lines]
      ]


print(sum((seq[p1-1] == l) ^ (seq[p2-1] == l) for [p1,p2,l,seq] in position_count_pairs))