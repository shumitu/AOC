from collections import defaultdict
from itertools import permutations
from timeit import default_timer as timer

def load_data(file):
    with open(file) as f:
        data = [[i for i in l.split()] for l in f.read().splitlines()]
        cities, distances_1, distances_2 = set(), defaultdict(int), defaultdict(int)
        for item in data:
            cities.update([item[0], item[2]])
        distances_1 = {(item[0], item[2]) : int(item[-1]) for item in data}
        distances_2 = {(item[2], item[0]) : int(item[-1]) for item in data}
        distances_1.update(distances_2)
        
        return cities, distances_1
    
def part12(cities, distances):
    size = len(cities)
    routes = list(permutations(cities, size))
    results = []
    for route in routes:
        sum = 0
        all_in = True
        for item in zip(route, route[1:]):
            if item in distances:
                sum += distances[item]
            else:
                all_in = False
                break
        if all_in: results.append(sum)
        
    return min(results), max(results)
 
 
time1 = timer()
cities, distances = load_data('data.txt')
part1, part2 = part12(cities, distances)
print(f"Part one: {part1}\nPart two: {part2}")
time2 = timer()
print(f"Execution time: {(time2 - time1)*1000:.3f}ms")