import itertools as it
from timeit import default_timer as timer

def load_data(file):
    antenas = {}
    with open(file, 'r') as f:
        data = [list(line) for line in f.read().splitlines()]
        width, height = len(data[0]), len(data)
        for i in range(width):
            for j in range(height):
                if data[i][j] != '.':
                    if data[i][j] not in antenas:
                        antenas[data[i][j]] = []
                    antenas[data[i][j]].append((i, j))
    return antenas, width, height
    
    
def part1(antenas, width, height):
    
    antinode_cords = set()
    
    for coords in antenas.values():
        for p1, p2 in it.permutations(coords, 2):
            dist = (p2[0] - p1[0], p2[1] - p1[1])
            antinode = (p2[0] + dist[0], p2[1] + dist[1])
            if  0 <= antinode[0] < width and 0 <= antinode[1] < height:
                antinode_cords.add(antinode)
    
    return len(antinode_cords)      


def part2(antenas, width, height):
    
    antinode_cords = set()
    
    for coords in antenas.values():
        for p1, p2 in it.permutations(coords, 2):
            dist = (p2[0] - p1[0], p2[1] - p1[1])
            # look at me, I am antinode now
            antinode = p1
            while True:
                antinode = (antinode[0] + dist[0], antinode[1] + dist[1])
                if  0 <= antinode[0] < width and 0 <= antinode[1] < height:
                    antinode_cords.add(antinode)
                else:
                    break
        
    return len(antinode_cords)       


antenas, width, height = load_data('data.txt')
start = timer()
print(f"Part one: {part1(antenas, width, height)}")
end = timer()
print(f"Part two: {part2(antenas, width, height)}")
end2 = timer()
print(f"Execution time part one: {(end - start) * 1000:.3f}ms")
print(f"Execution time part one: {(end2 - end) * 1000:.3f}ms")