def load_data(file):
    with open(file, 'r') as f:
        return [[int(i) for i in l.split("x")] for l in f.read().splitlines()]
    

def part1(data):
    return sum(2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l]) for l,w,h in data)


def part2(data):
    sum = 0
    for box in data:
        l, w, h = sorted(box)
        sum += 2*l + 2*w + l*w*h # not really l,w,h but who cares
    return sum


data = load_data('data.txt')
print(f"Part one: {part1(data)}")
print(f"Part two: {part2(data)}")
