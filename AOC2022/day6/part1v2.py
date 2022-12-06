import sys


def read_input(file):
    with open(file, 'r') as f:
        return f.readline()

def find_marker(input_str, offset):
    for index in range(len(input_str)):
        if len(set(input_str[index - offset:index])) == offset:
            print(f'Index for offset {offset} is: {index}')
            break


if __name__ == '__main__':
    input_str = read_input(sys.argv[1])
    find_marker(input_str, 4)
    find_marker(input_str, 14)

