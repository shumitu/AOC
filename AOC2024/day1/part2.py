from collections import Counter

def calculate(file):
    with open(file, 'r') as f:
        lst = [l.split() for l in f.readlines()]
        left = [int(n[0]) for n in lst]
        right = [int(n[1]) for n in lst]
        c = Counter(right)
        sum = 0
        for n in left:
            sum += n * c[n]
        print(sum)

calculate('data.txt')