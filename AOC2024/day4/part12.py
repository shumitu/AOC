import numpy as np


def load_data(file):
    with open(file, 'r') as f:
        return np.array([list(row) for row in f.read().splitlines()])


def part1(array):
    pattern = "XMAS"
    _, height = len(array[0]), len(array)
    sum = 0
    for row in range(height):
        s_row = ''.join(array[row])
        s_col = ''.join(array[:, row])
        
        sum += s_row.count(pattern)
        sum += s_col.count(pattern)
        sum += s_row.count(pattern[::-1])
        sum += s_col.count(pattern[::-1])

    arr_flip = np.fliplr(array)
    # Diagonals
    for i in range(-height + 1, height):
        sum += ''.join(array.diagonal(i)).count(pattern)
        sum += ''.join(array.diagonal(i)).count(pattern[::-1])
    # Anti diagonals
        sum += ''.join(arr_flip.diagonal(i)).count(pattern)
        sum += ''.join(arr_flip.diagonal(i)).count(pattern[::-1])

    return sum


def part2(array):
    _, height = len(array[0]), len(array)
    sum = 0
    for i in range(1, height - 1):
        for j in range(1, height - 1):
            if array[i][j] == 'A':
                
                ul = array[i - 1][j - 1]
                ur = array[i - 1][j + 1]
                dl = array[i + 1][j - 1]
                dr = array[i + 1][j + 1]
                
                if ul == 'M' and dr == 'S' and dl == 'M' and ur == "S":
                    sum += 1
                elif ul == 'M' and dr == 'S' and dl == 'S' and ur == "M": 
                    sum += 1
                elif ul == 'S' and dr == 'M' and dl == 'M' and ur == "S":
                    sum += 1
                elif ul == 'S' and dr == 'M' and dl == 'S' and ur == "M":
                    sum += 1
    return sum


array = load_data('data.txt')
print(f"Part one: {part1(array)}")
print(f"Part two: {part2(array)}")
