def load_data(file):
    with open(file, 'r') as f:
        return f.read()
    

def part1(data):
    dir = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}
    p, houses = (0, 0), set()
    houses.add(p)
    for c in data:
        p_new = (p[0] + dir[c][0], p[1] + dir[c][1])
        houses.add(p_new)
        p = p_new

    return len(set(houses))


def part2(data):
    dir = {'<': (0, -1), '^': (-1, 0), '>': (0, 1), 'v': (1, 0)}
    p, p_robo, houses = (0, 0), (0, 0), set()
    houses.add(p)
    
    for idx, c in enumerate(data):
        if idx % 2 == 0:
            p_new = (p[0] + dir[c][0], p[1] + dir[c][1])
            houses.add(p_new)
            p = p_new
        else:
            p_robo_new = (p_robo[0] + dir[c][0], p_robo[1] + dir[c][1])
            houses.add(p_robo_new)
            p_robo = p_robo_new         

    return len(houses)

data = load_data('data.txt')
print(f"Part one: {part1(data)}")
print(f"Part two: {part2(data)}")