import sys

# y - paper, x - rock, z - scissors
# a - rock, b - paper, c - scissors 
weights = {
    'Z': 3,
    'Y': 2,
    'X': 1,
}
outcome = {
    ('C', 'Z'): 3,
    ('B', 'Y'): 3,
    ('A', 'X'): 3,
    ('C', 'X'): 6,
    ('B', 'Z'): 6,
    ('A', 'Y'): 6,
    ('C', 'Y'): 0,
    ('B', 'X'): 0,
    ('A', 'Z'): 0
}

def calculate_score(file):
    data = []
    sum = 0
    with open(file, 'r') as f:
        data = f.read().splitlines()
    for round in data:
        sum += weights[round.split()[1]] + outcome[(round.split()[0], round.split()[1])] 
    print(sum)


if __name__ == '__main__':
    calculate_score(sys.argv[1])