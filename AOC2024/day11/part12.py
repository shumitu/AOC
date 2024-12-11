from collections import Counter, defaultdict
from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return [int(i) for i in f.read().split()]
    

def blink_blink(stones, blinks):

    counter = Counter(stones)

    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone, count in counter.items():
            if stone == 0:
                new_stones[1] += count
            elif len(tmp_str := str(stone)) % 2 == 0:
                left_stone = int(tmp_str[:len(tmp_str) // 2])
                right_stone = int(tmp_str[len(tmp_str) // 2 :])
                new_stones[left_stone] += count
                new_stones[right_stone] += count
            else:
                new_stones[stone * 2024] += count
        
        counter = new_stones
    # print(counter)
    
    return sum(counter.values())
            
time1 = timer()
stones = load_data('data.txt')
time2 = timer()
print(f"Part one: {blink_blink(stones, 25)}")
time3 = timer()
print(f"Part two: {blink_blink(stones, 75)}")
time4 = timer()
print(f"Data load time: {(time2 - time1) * 1000:.3f}ms")
print(f"Part one execution time: {(time3 - time2) * 1000:.3f}ms")
print(f"Data two execution time: {(time4 - time3) * 1000:.3f}ms")

