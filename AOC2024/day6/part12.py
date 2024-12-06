from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return [list(row) for row in f.read().splitlines()]
    
# Generator goes brrrt
def get_direction(directions):
    while True:
        for direction in directions:
            yield direction
            
            
def get_cords(array, arg = '^'):
    width, height = len(array[0]), len(array)
    for i in range(width):
        for j in range(height):
            if array[i][j] == arg:
                return i, j, width, height
               
            
def part1(array):
    # directions: up -> right -> down -> left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = get_direction(directions)
    current_direction = next(direction)

    i, j, width, height = get_cords(array=array)
    
    visited = set()
        
    while i >= 0 and i < width and j >= 0 and j < height:
        
        i_new, j_new = i + current_direction[0], j + current_direction[1]
                
        while i_new >= 0 and i_new < width and j_new >= 0 and j_new < height:

            if array[i_new][j_new] == "#":
                current_direction = next(direction)
                i_new, j_new = i + current_direction[0], j + current_direction[1]
            else:
                break
        
        visited.add((i, j))
        i, j = i_new, j_new
            
    return len(visited)


def part2_solve(array, i_obst, j_obst, i, j, width, height, directions):
    visited = set()
    direction = get_direction(directions)
    current_direction = next(direction)
    
    while i >= 0 and i < width and j >= 0 and j < height:
        
        previous_direction = current_direction
        i_new, j_new = i + current_direction[0], j + current_direction[1]
        
        while i_new >= 0 and i_new < width and j_new >= 0 and j_new < height:

            if array[i_new][j_new] == "#" or (i_new, j_new) == (i_obst, j_obst):
                current_direction = next(direction)
                i_new, j_new = i + current_direction[0], j + current_direction[1]
            else:
                break
        
        visited.add(((i, j) + previous_direction))
        i, j = i_new, j_new
        if ((i_new, j_new) + current_direction) in visited: 
            return True
    
    return False
    
    
def part2(array):
    # directions: up -> right -> down -> left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    i, j, width, height = get_cords(array=array)
    
    sum = 0
    
    for i_obst in range(width):
        for j_obst in range(height):
            if array[i_obst][j_obst] == ".":
                sum += int(part2_solve(array, i_obst, j_obst, i, j, width, height, directions))
                                        
    return sum            

start = timer()
array = load_data('data.txt')
print(f"Part one: {part1(array)}")
print(f"Part two: {part2(array)}")
end = timer()
print(f"execution time: ", end - start, "s")
