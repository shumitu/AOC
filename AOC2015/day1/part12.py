def load_data(file):
    with open(file, 'r') as f:
        return f.read()
    

def part1(data):
    return sum(1 if c == "(" else -1 for c in data)


def part2(data):
    sum = 0
    for idx, c in enumerate(data, 1):
        sum += 1 if c == "(" else -1
        if sum < 0: return idx

data = load_data('data.txt')
print(f"Part one: {part1(data)}")
print(f"Part two: {part2(data)}")