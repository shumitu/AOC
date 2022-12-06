import sys


def find_marker(file):
    input_str = ''
    with open(file, 'r') as f:
        input_str = f.readline()

    # part 1
    for index, _ in enumerate(input_str):
        if len(set(input_str[index - 4:index])) == 4:
            print(f'Index for part 1: {index}')
            break

    # part 2
    for index, _ in enumerate(input_str):
        if len(set(input_str[index - 14:index])) == 14:
            print(f'Index for part 2: {index}')
            break


if __name__ == '__main__':
    find_marker(sys.argv[1])
