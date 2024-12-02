def load_data(file):
    with open(file, 'r') as f:
        return [[int(n) for n in l.split()] for l in f.readlines()]


def is_fine(row):
    if all(i < j and 0 < j - i < 4 for i, j in zip(row, row[1:])):
        return True
    elif all(i > j and 0 < i - j < 4 for i, j in zip(row, row[1:])):
        return True
    return False


def check_part1(data):
    return sum(1 for row in data if is_fine(row))


def check_part2(data):
    sum = 0
    for row in data:
        if is_fine(row):
            sum += 1
        else:
            for i in range(len(row)):
                if is_fine(row[:i] + row[i+1:]):
                    sum += 1
                    break
    return sum


data = load_data('data.txt')
print(f"Part 1: {check_part1(data)}")
print(f"Part 2: {check_part2(data)}")
