
instructions_map = {}
map_copy = {}


def save_map():
    global map_copy
    map_copy = instructions_map.copy()

def reset_map():
    global instructions_map
    instructions_map = map_copy.copy()

def filter_jmp_nop(item):
    [key, p] = item
    if p[0] == 'jmp' or p[0] == 'nop':
        return True
    else:
        return False

def run_program():
    accumulator = 0
    i = 0   
    while True:
        (cmd, cmd_nbr, execs) = instructions_map[i]
        if execs > 0:
            #Program failed
            break
        else:
            #Update instr as executed
            instructions_map[i] = (cmd, cmd_nbr, execs + 1)

        if cmd == 'acc':
            accumulator += cmd_nbr
            i += 1

        elif cmd == 'jmp':
            i += cmd_nbr

        elif cmd == 'nop':
            i += 1
        
        if i == len(instructions_map):
            #Program finished correctly
            return accumulator
    return -1

file = open('input.txt', 'r') 
lines = file.readlines()


for ins_nbr, line in enumerate(lines):
    [ins, val] = line.strip().strip('\n').split(' ')
    instructions_map[ins_nbr] = (ins, int(val[1:]) if val[1:] == '+' else int(val), 0)

save_map()
nop_jmp_indexes = filter(filter_jmp_nop, instructions_map.items())
for idx, p in nop_jmp_indexes:
    reset_map()
    if p[0] == 'jmp':
        instructions_map[idx] = ('nop', p[1], 0)
    elif p[0] == 'nop':
        instructions_map[idx] = ('jmp', p[1], 0)
    
    accumulator = run_program()
    if accumulator > 0:
        print(accumulator)
        break







    

    
