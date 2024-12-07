from timeit import default_timer as timer

ADD = lambda a, b: a + b
MUL = lambda a, b: a * b
CON = lambda a, b: int(f'{a}{b}')
OPS_PART1 = [ADD, MUL]
OPS_PART2 = [ADD, MUL, CON]


def load_data(file):
    with open(file, 'r') as f:
        return [[int(i) for i in l.replace(':', '').split()] for l in f.read().splitlines()]


def val_str(value, elems):
    if len(elems) == 1:
        return value == elems[0]
    for action in OPS_PART1:
        val = action(*elems[:2])
        if val_str(value, [val, *elems[2:]]):
            return True
    return False
    

def val_str2(value, elems):
    if len(elems) == 1:
        return value == elems[0]
    for action in OPS_PART2:
        val = action(*elems[:2])
        if val_str2(value, [val, *elems[2:]]):
            return True
    return False


def part1(data):
    return sum(line[0] for line in data if val_str(line[0], line[1:]))


def part2(data):
    return sum(line[0] for line in data if val_str2(line[0], line[1:]))


start = timer()
data = load_data('data.txt')
print(f"Part one: {part1(data)}")
print(f"Part two: {part2(data)}")

end = timer()
print(f"Execution time: {end - start:.3f}s")