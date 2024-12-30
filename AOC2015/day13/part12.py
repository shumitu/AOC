from itertools import permutations
from collections import defaultdict
from timeit import default_timer as timer


def load_data(file):
    with open(file, "r") as f:
        rules = defaultdict(int)
        tmp = [l.split() for l in f.read().splitlines()]
        # {(name1, name2): value} - if 'gain': +, else -
        # rules = {(e[0], e[-1].rstrip(".")):int(e[3]) if e[2] == "gain" else -int(e[3]) for e in tmp}
        for e in tmp:
            rules[(e[0], e[-1].rstrip("."))] = int(e[3]) if e[2] == "gain" else -int(e[3])
        
        names = set([e[0] for e in tmp])

        return rules, names
        
        
def part12(rules, names):
    perm = permutations(names, len(names))
    # Extend tuples to have table where last elem is same as first elem
    tables = [(*e, e[0]) for e in perm]
    sum_part1 = (max(sum(rules[k] + rules[k[::-1]] for k in zip(table, table[1:])) for table in tables))
    
    names.add("Its a me, Mario!")
    perm = permutations(names, len(names))
    tables = [(*e, e[0]) for e in perm]
    sum_part2 = (max(sum(rules[k] + rules[k[::-1]] for k in zip(table, table[1:])) for table in tables))
    
    return sum_part1, sum_part2
    
time = timer()            
rules, names = load_data("data.txt")
sum_part1, sum_part2 = part12(rules, names)
time2 = timer()
print(f"Part one: {sum_part1}")
print(f"Part two: {sum_part2}")
print(f"Execution time: {(time2 - time) * 1000:.3f}ms")