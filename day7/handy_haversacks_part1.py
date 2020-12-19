import functools

#Define global index
bag_tree_index = {}

def recursive_has_shiny_bag(bag_key):
    bags = bag_tree_index[bag_key].keys()

    if 'shiny gold' in bags:
        return True

    for key in bags:
        if recursive_has_shiny_bag(key):
            return True
    
    return False
    

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

print(sum([recursive_has_shiny_bag(bag_key) for bag_key in bag_tree_index.keys()]))





    

    
