import sys


def calculate(file):
    data = []
    with open(file) as f:
        data = [(x.split()[0], int(x.split()[1]))
                for x in f.read().splitlines()]

    sum_forward = sum(x[1] for x in list(filter(lambda x: x[0] == 'forward', data)))
    sum_up = sum(x[1] for x in list(filter(lambda x: x[0] == 'up', data)))
    sum_down = sum(x[1] for x in list(filter(lambda x: x[0] == 'down', data)))
    print(sum_forward, sum_down - sum_up, sum_forward * (sum_down - sum_up))


if __name__ == '__main__':
    calculate(sys.argv[1])
