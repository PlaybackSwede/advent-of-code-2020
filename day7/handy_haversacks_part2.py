import functools

#Define global index
bag_tree_index = {}

def recursive_bags_in_bag(bag_key):
    bag_nbr_pairs = bag_tree_index[bag_key].items()
    if len(bag_nbr_pairs) == 0:
        return 1
    
    nbr_bags = 0
    for key, nbr in bag_nbr_pairs:
        if len(bag_tree_index[key]) == 0:
            nbr_bags += recursive_bags_in_bag(key)*nbr
        else:
            nbr_bags += nbr + recursive_bags_in_bag(key)*nbr

    return nbr_bags
    

file = open('input.txt', 'r') 
lines = file.readlines()

i = 0
for line in lines:  
    words = line.strip().split("bags contain")
    color_key = words[0].strip()
    bags_str = words[1].strip()

    if not bag_tree_index.get(color_key):
        bag_tree_index[color_key] = {}
    
    if bags_str == "no other bags.":
        continue

    for bag_str in bags_str.split(", "):
        color_bags = bag_str.strip().strip('.').strip('bag').strip('bags').split(' ')

        bag_nbr = int(color_bags[0])
        bag_color_key = color_bags[1] + ' ' + color_bags[2]
        
        bag_tree_index[color_key][bag_color_key] = bag_nbr

print(recursive_bags_in_bag('shiny gold'))





    

    
