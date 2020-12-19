EXECUTIONS = 2

instructions_map = {}

def run_program():
    accumulator = 0
    i = 0
    while instructions_map[i][EXECUTIONS] == 0:
        (cmd, cmd_nbr, execs) = instructions_map[i]
    
        #Update nbr executions
        instructions_map[i] = (cmd, cmd_nbr, execs + 1)

        if cmd == 'acc':
            accumulator += cmd_nbr
            i += 1

        elif cmd == 'jmp':
            i += cmd_nbr

        elif cmd == 'nop':
            i += 1

    return accumulator


file = open('input.txt', 'r') 
lines = file.readlines()


for ins_nbr, line in enumerate(lines):
    [ins, val] = line.strip().strip('\n').split(' ')
    instructions_map[ins_nbr] = (ins, int(val[1:]) if val[1:] == '+' else int(val), 0)


print(run_program())






    

    
