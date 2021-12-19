import sys


def how_many(input):
    data = []
    with open(input) as f:
        data = [int(x) for x in f.read().splitlines()]

    increased = 0
    triple_sums = [sum([data[i], data[i+1], data[i+2]])
                   for i in range(len(data) - 2)]
    for i in range(1, len(triple_sums)):
        if triple_sums[i] > triple_sums[i-1]:
            increased += 1

    print(increased)


if __name__ == '__main__':
    how_many(sys.argv[1])
