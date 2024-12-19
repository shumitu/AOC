from timeit import default_timer as timer
from collections import defaultdict

def load_data(file):
    with open(file, 'r') as f:
        data = []
        for line in f.read().splitlines():
            if line.startswith('toggle'):
                op, start, _, end = line.split()
            elif line.startswith('turn'):
                _, op, start, _, end = line.split()
            start_x, start_y = start.split(',')
            end_x, end_y = end.split(',')
            data.append((op, int(start_x), int(start_y), int(end_x), int(end_y)))

    return data        


def part1(data):
    arr = defaultdict(bool)
    # operation, x, y, end_x, end_y
    for op, start_x, start_y, end_x, end_y in data:
        # print(op, start_x, start_y, end_x, end_y)
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                match op:
                    case 'on':
                        arr[(i, j)] = True
                    case 'off':
                        arr[(i, j)] = False
                    case 'toggle':
                        arr[(i, j)] = not arr[(i, j)]
    
    return sum(1 for value in arr.values() if value)
        

def part2(data):
    arr = defaultdict(int)
    # operation, x, y, end_x, end_y
    for op, start_x, start_y, end_x, end_y in data:
        # print(op, start_x, start_y, end_x, end_y)
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                match op:
                    case 'on':
                        arr[(i, j)] += 1
                    case 'off':
                        arr[(i, j)] -= 1 if arr[(i, j)] > 0 else 0
                    case 'toggle':
                        arr[(i, j)] += 2
    
    return sum(value for value in arr.values())
    
    
time = timer()
data = load_data('data.txt')
print(f"Part one: {part1(data)}")
print(f"Part two: {part2(data)}")
time2 = timer()
print(f"Execution time: {time2 - time:.3f}s")