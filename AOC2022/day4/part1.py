import sys


def check_sublist(file):
    with open(file, 'r') as f:
        data = [x.split(',') for x in f.read().splitlines()]
        combined = [entry[0].split('-') + entry[1].split('-') for entry in data]
        sum = 0
        for entry in combined:
            if (int(entry[0]) <= int(entry[2])) and (int(entry[1]) >= int(entry[3])):
                sum += 1
            elif (int(entry[0]) >= int(entry[2])) and (int(entry[1]) <= int(entry[3])):
                sum += 1
        print(sum)


if __name__ == '__main__':
    check_sublist(sys.argv[1])
