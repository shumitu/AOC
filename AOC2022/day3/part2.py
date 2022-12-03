import sys
import string


def calculate_priority(file):
    priority_values = {letter: priority+1 for priority,
                       letter in enumerate(string.ascii_lowercase + string.ascii_uppercase)}
    with open(file, 'r') as f:
        data = [row for row in f.read().splitlines()]
        chunks = [data[x:x+3] for x in range(0, len(data), 3)]
        badges = [next(iter(set(entry[0]).intersection(entry[1]).intersection(entry[2]))) for entry in chunks]

        print(sum(priority_values[badge] for badge in badges))


if __name__ == '__main__':
    calculate_priority(sys.argv[1])
