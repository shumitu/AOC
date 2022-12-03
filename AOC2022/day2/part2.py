import sys

# y - paper, x - rock, z - scissors
# a - rock, b - paper, c - scissors 
# X - loose 0, Y - draw 3, Z - win 6
# 
weights = {
    'Z': (3, 6),
    'Y': (2, 3),
    'X': (1, 0)
}

results = {
    ('C', 'Z'): 'X',
    ('B', 'Y'): 'Y',
    ('A', 'X'): 'Z',
    ('C', 'X'): 'Y',
    ('B', 'Z'): 'Z',
    ('A', 'Y'): 'X',
    ('C', 'Y'): 'Z',
    ('B', 'X'): 'X',
    ('A', 'Z'): 'Y'
}

def calculate_score(file):
    data = []
    sum = 0
    with open(file, 'r') as f:
        data = f.read().splitlines()
    for round in data:
        sum += weights[results[tuple(round.split())]][0] + weights[round.split()[1]][1]
    print(sum)

if __name__ == '__main__':
    calculate_score(sys.argv[1])