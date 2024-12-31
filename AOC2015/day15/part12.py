from itertools import product
from timeit import default_timer as timer

def load_data(file):
    with open(file, "r") as f:
        tmp = [[e.rstrip(",") for e in l.split()] for l in f.read().splitlines()]
    # capacity, durability, flavor, texture, calories 
    # return [[int(e[2]), int(e[4]), int(e[6]), int(e[8]), int(e[10])] for e in tmp]
    return [[int(e[i]) for i in range(2, 12, 2)] for e in tmp]
    

def part12(ingredients, spoons):
    sums = []
    ratios = [r for r in product(range(1, spoons), repeat=len(ingredients)) if sum(r) == 100]
    for ratio in ratios:
        
        cap_sum, dur_sum, flav_sum, text_sum, cal_sum = 0, 0, 0, 0, 0
        
        for idx, (capacity, durability, flavor, texture, calories) in enumerate(ingredients):
            cap_sum += ratio[idx] * capacity
            dur_sum += ratio[idx] * durability
            flav_sum += ratio[idx] * flavor
            text_sum += ratio[idx] * texture
            cal_sum += ratio[idx] * calories
            
        local_sum = 1
        for var in [cap_sum, dur_sum, flav_sum, text_sum]:
            local_sum *= var if var > 0 else 0
        
        sums.append((local_sum, cal_sum))

    return max(s[0] for s in sums), max(s[0] for s in filter(lambda x: x[1] == 500, sums))
        
            
time = timer()
ingredients = load_data("data.txt")
part1, part2 = part12(ingredients, 100)
print(f"Part one: {part1}")
print(f"Part two: {part2}")
time2 = timer()
print(f"Execution time: {(time2 - time):.3f}s")