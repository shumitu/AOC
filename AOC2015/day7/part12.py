from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return [l.split() for l in f.read().splitlines()]
    
    
def part12(data, value = 0):
    commands = data.copy()
    wires = {}
    if value != 0: wires['b'] = value
    while commands:
        for line in commands:
            if line[0] == 'NOT':
                if line[1] in wires and line[-1] not in wires:
                    wires[line[-1]] = ~ wires[line[1]] & 0xFFFF
                    del(commands[commands.index(line)])
                    
            else:   
                
                if line[0].isdigit():
                    tmp_l = int(line[0])
                elif line[0] in wires:
                    tmp_l = wires[line[0]]
                else: 
                    continue
                
                if len(line) == 5:
                    if line[2].isdigit():
                        tmp_r = int(line[2])
                    elif line[2] in wires:
                        tmp_r = wires[line[2]]
                    else: 
                        continue
                    
                if line[-1] not in wires:
                    match line[1]:
                        case '->': 
                            wires[line[-1]] = tmp_l & 0xFFFF
                            del(commands[commands.index(line)])
                        case 'AND':
                            wires[line[-1]] = tmp_l & tmp_r & 0xFFFF
                            del(commands[commands.index(line)])
                        case 'OR':
                            wires[line[-1]] = tmp_l | tmp_r & 0xFFFF
                            del(commands[commands.index(line)])
                        case 'LSHIFT':
                            wires[line[-1]] = tmp_l << tmp_r & 0xFFFF
                            del(commands[commands.index(line)])
                        case 'RSHIFT':
                            wires[line[-1]] = tmp_l >> tmp_r & 0xFFFF
                            del(commands[commands.index(line)])
                else: del(commands[commands.index(line)])

    return wires


time = timer()
data = load_data('data.txt')
wires = part12(data)
print(f"Part one: {wires['a']}")
wires = part12(data, wires['a'])
print(f"Part two: {wires['a']}")
time2 = timer()
print(f"Execution time: {(time2 - time)*1000:.3f}ms")