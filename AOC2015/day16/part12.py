from timeit import default_timer as timer


def load_data(file):
    with open(file) as f:
        tmp = [l.split() for l in f.read().splitlines()]
        dicts = []
        for e in tmp:
            dct = dict()
            # Sue 1: goldfish: 6, trees: 9, akitas: 0
            # In loop gets only: goldfish: 6, trees: 9, akitas: 0
            for i in range(3, 9, 2):
                dct[e[i - 1]] = e[i].rstrip(",")
            dicts.append((int(e[1].rstrip(":")), dct))

    return dicts


def parse_pattern(string):
    pattern_dct = dict()
    for l in string.splitlines():
        k, v = l.split()
        pattern_dct[k] = v

    return pattern_dct

    
def part1(dicts, pattern):
    for i, dct in dicts:
        if dct.items() <= pattern.items():
            return i
    
    
def part2(dicts, pattern):
    for i, dct in dicts:
        is_subset = True
        for k, v in dct.items():
            if k in pattern and k in ["cats:", "trees:"]:
                if not dct[k] > pattern[k]: is_subset = False
            elif k in pattern and k in ["pomeranians:", "goldfish:"]:
                if not dct[k] < pattern[k]: is_subset = False
            elif (k, v) not in pattern.items():
                is_subset = False
        
        if is_subset: return i
                          

time = timer()
pattern = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
data = load_data("data.txt")
pattern = parse_pattern(pattern)
print(f"Part one: {part1(data, pattern)}")
print(f"Part one: {part2(data, pattern)}")
time2 = timer()
print(f"Execution time: {(time2 - time) * 1000:.3f}ms")