import sys


def how_many(input):
    data = []
    with open(input) as f:
        data = [int(x) for x in f.read().splitlines()]
    increased = 0
    for i in range(1, len(data)):
       if data[i] > data[i - 1]:
        increased += 1
    print(increased)


if __name__ == '__main__':
    how_many(sys.argv[1])
