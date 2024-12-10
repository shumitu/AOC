from collections import deque
from timeit import default_timer as timer 

def load_data(file):
    with open(file, 'r') as f:
        trailheads = deque()
        arr = [[int(i) for i in list(line)] for line in f.read().splitlines()]
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    trailheads.append((i, j))

    return arr, trailheads


def solve(arr, trailheads):
    # up -> right -> down -> left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    height, width = len(arr), len(arr[0])
    
    sum_part1, sum_part2 = 0, 0

    for head in trailheads:
        target = []
        frontier = deque()
        frontier.append(head)
        # visited = set() # DFS thingy but will break part2
        while frontier:
            i, j = frontier.pop()
            if arr[i][j] == 9: target.append((i, j))
            # if (i, j) in visited: # DFS thingy but will break part2
            #     continue
            for d in directions:
                i_n, j_n = i + d[0], j + d[1]
                if 0 <= i_n < height and 0 <= j_n < width and arr[i_n][j_n] - arr[i][j] == 1:
                    frontier.append((i_n, j_n))
            
            # visited.add((i, j)) # DFS thingy but will break part2
                    
        sum_part1 += len(set(target))
        sum_part2 += len(target)
    
    print(f"Part one: {sum_part1}\nPart two: {sum_part2}")        


start = timer()
arr, trailheads = load_data('data.txt')
solve(arr, trailheads)
end = timer()
print(f"Execution time: {(end - start)*1000:.3f}ms")
