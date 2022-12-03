import sys
from collections import Counter


def calculate(file):
    data = []
    with open(file) as f:
        data = f.read().splitlines()
    sums = [[x[i] for x in data] for i in range(len(data[0]))]
    gamma_binnary = [Counter(x).most_common()[0][0] for x in sums]
    epsilon_binnary = [Counter(x).most_common()[1][0] for x in sums]

    print(int(''.join(gamma_binnary), 2) * int(''.join(epsilon_binnary), 2))


if __name__ == '__main__':
    calculate(sys.argv[1])
