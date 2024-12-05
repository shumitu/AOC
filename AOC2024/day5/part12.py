def load_data(file):
    with open(file, 'r') as f:
       data = f.read().splitlines()
       idx = data.index('')
       rules = [[int(i) for i in r.split('|')] for r in data[:idx]]
       pages = [[int(i) for i in r.split(',')] for r in data[idx + 1:]]
       return rules, pages
        

def validate(rules, line):
    status = True
    for rule in rules:
        if all(single_rule in line for single_rule in rule):
            if line.index(rule[0]) < line.index(rule[1]):
                continue
            else:
                status = False
    return status


def fix(rules, line):
    loop = True
    while loop:
        loop = False
        for rule in rules:
            if all(page in line for page in rule):
                idx0, idx1 = line.index(rule[0]), line.index(rule[1])
                if not idx0 < idx1:
                    line[idx0], line[idx1] = line[idx1], line[idx0]
                    loop = True   
    
    return line     
                
                
def part1(rules, pages):
    valid_lines = []
    not_valid_lines = []
    for line in pages:
        if validate(rules, line):
            valid_lines.append(line)
        else:
            not_valid_lines.append(line) 
            
    return sum(line[len(line) // 2] for line in valid_lines), not_valid_lines
        
        
def part2(rules, not_valid_lines):
    fixed = [fix(rules, line) for line in not_valid_lines]
    return sum(line[len(line) // 2] for line in fixed)
    

rules, pages = load_data('data.txt')
part1_sum, not_valid_lines = part1(rules, pages)
part2_sum = part2(rules, not_valid_lines)
print(f"Part one: {part1_sum}")
print(f"Part two: {part2_sum}")

