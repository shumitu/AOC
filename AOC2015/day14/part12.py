from timeit import default_timer as timer

def load_data(file):
    with open(file, "r") as f:
        tmp = [l.split() for l in f.read().splitlines()]
        # Reindeer: [speed, fly_time, rest_time, distance, matrix]
        return [[int(e[3]), int(e[6]), int(e[13]), 0, []] for e in tmp]

        
def part1(deers, time):
    # Reindeer: [speed, fly_time, rest_time, distance, matrix]
    for deer in deers:
        run_time = time
        while run_time > 0:
            if run_time - deer[1] >= 0:
                deer[3] += deer[0] * deer[1]
                deer[4].extend([True for _ in range(deer[1])]) 
                run_time = run_time - deer[1]
                if run_time - deer[2] >= 0:
                    run_time = run_time - deer[2] 
                    deer[4].extend([False for _ in range(deer[2])]) 
                else: 
                    deer[4].extend([False for _ in range(run_time)]) 
                    break
            else: 
                deer[4].extend([False for _ in range(run_time)]) 
                break
    
    return max(v[3] for v in deers)


def part2(deers, time):
    # Reindeer: [speed, fly_time, rest_time, distance, score, matrix]
    # Set distance and score to 0
    deers = [[e[0], e[1], e[2], 0, 0, e[4]] for e in deers]
    run_time = time
    i = 0
    while i < run_time:
        for deer in deers:
            if deer[5][i]: # if True -> +distance
                deer[3] += deer[0] # distance += speed
        # Get max of distances for all deers        
        mx = max(deer[3] for deer in deers)
        for deer in deers:
            if deer[3] == mx:
                deer[4] += 1 # Increment score for max distance deers
              
        i += 1
                
    return max(v[4] for v in deers)


time = timer()
reindeers = load_data("data.txt")
print(f"Part one: {part1(reindeers, 2503)}")
print(f"Part two: {part2(reindeers, 2503)}")
time2 = timer()
print(f"Execution time: {(time2 - time) * 1000:.3f}ms")