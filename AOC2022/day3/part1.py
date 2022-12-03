import sys
import string


def calculate_priority(file):
    priority_values = {letter: priority+1 for priority,
                       letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    with open(file, 'r') as f:
        data = [[row[:len(row)//2], row[len(row)//2:]] for row in f.read().splitlines()]
        repeated_items = [next(iter(set(row[0]).intersection(row[1]))) for row in data]

        print(sum(priority_values[item] for item in repeated_items))


if __name__ == '__main__':
    calculate_priority(sys.argv[1])
