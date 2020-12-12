

file = open('input.txt', 'r') 
lines = file.readlines()


range_count_pairs = [
        [int(arr[0].split('-')[0]), 
        int(arr[0].split('-')[1]), 
        arr[2].count(arr[1][0])] 
        for arr in [line.strip().split(' ') for line in lines]
      ]


print(sum(count <= ub and count >= lb for [lb,ub,count] in range_count_pairs))