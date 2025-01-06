from copy import deepcopy
from timeit import default_timer as timer

def load_data(file):
    with open(file, "r") as f:
        return [list(l) for l in f.read().splitlines()]
    

def live_neighbours(x, y, matrix):
    # left, up, right, down, left-up, right-up, left-down, right-down
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    live, width, height = 0, len(matrix[0]), len(matrix)
    for dx, dy in directions:
        if 0 <= x + dx < height and 0 <= y + dy < width:
            if matrix[x + dx][y + dy] == "#" or matrix[x + dx][y + dy] == False: # is live / will die in next
                live += 1
    return live


def part12(matrix, n, do_part_two = False):
    matrix = deepcopy(matrix)
    width, height = len(matrix[0]), len(matrix)

    if do_part_two:
        for (i, j) in [(0, 0), (0, width - 1), (height - 1, 0), (width - 1, height -1)]:   
            matrix[i][j] = "#"  
    
    for _ in range(n):        
        for i in range(width):
            for j in range(height):
                live = live_neighbours(i, j, matrix)
                if matrix[i][j] == "#" and live not in [2, 3]:
                    matrix[i][j] = False
                elif matrix[i][j] == "." and live == 3:
                    matrix[i][j] = True
                    
        for i in range(width):
            for j in range(height):
                if matrix[i][j] == True:
                    matrix[i][j] = "#"
                if matrix[i][j] == False:
                    matrix[i][j] = "."
                    
        if do_part_two:
            for (i, j) in [(0, 0), (0, width - 1), (height - 1, 0), (width - 1, height -1)]:   
                matrix[i][j] = "#"   
                                        
    return sum(1 for j in range(height) for i in range(width) if matrix[i][j] == "#")


time = timer()
matrix = load_data("data.txt")
print(f"Part one: {part12(matrix, 100)}")
print(f"Part two: {part12(matrix, 100, do_part_two=True)}")
time2 = timer()
print(f"Execution time: {(time2 - time):.2f}s")