from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return [list(row) for row in f.read().splitlines()]
    
            
def get_cords(array, arg = '^'):
    width, height = len(array[0]), len(array)
    for i in range(width):
        for j in range(height):
            if array[i][j] == arg:
                return i, j, width, height
               
            
def part1(array):
    # directions: up -> right -> down -> left
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    index = 0

    i, j, width, height = get_cords(array=array)
    
    visited = set()
    visited.add((i, j))
        
    while True:
        i_new, j_new = i + dir[index][0], j + dir[index][1]
        if (i_new < 0 or i_new >= width) or (j_new < 0 or j_new >= height):
            return visited
        
        elif array[i_new][j_new] == "#":
            index = (index + 1) % 4 
            continue
        
        i, j = i_new, j_new 
        visited.add((i, j))
    
        
        
def part2_loop(array, i, j, width, height, i_obst, j_obst):
    # directions: up -> right -> down -> left
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    index = 0
    visited = set()
    visited.add((i, j) + dir[index])
        
    while True:
        i_new, j_new = i + dir[index][0], j + dir[index][1]
        if (i_new < 0 or i_new >= width) or (j_new < 0 or j_new >= height):
            return False
        
        elif array[i_new][j_new] == "#" or (i_obst, j_obst) == (i_new, j_new):
            index = (index + 1) % 4 
            continue
        
        i, j = i_new, j_new 
        if ((i, j) + dir[index]) in visited:
            return True
        else:
            visited.add((i, j) + dir[index])


def part2(array, paths):
    i, j, width, height = get_cords(array=array)
    sum = 0
    for path in paths:
        sum += int(part2_loop(array, i, j, width, height, path[0], path[1]))
    return sum
                

start = timer()
array = load_data('data.txt')
part1_result = part1(array)
print(f"Part one: {len(part1_result)}")
print(f"Part two: {part2(array, part1_result)}")
end = timer()
print(f"execution time: { end - start:.3f}s")
