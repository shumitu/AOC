import sys


def calculate(file):
    data = []
    aim = 0
    forward = 0
    depth = 0
    with open(file) as f:
        data = [(x.split()[0], int(x.split()[1]))
                for x in f.read().splitlines()]

    for step in data:
        match step[0]:
            case 'forward':
                forward += step[1]
                depth += aim * step[1]
            case 'down':
                aim += step[1]
            case 'up':
                aim -= step[1]

    print(forward, depth, aim, forward * depth)


if __name__ == '__main__':
    calculate(sys.argv[1])
