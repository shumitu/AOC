import sys
from itertools import groupby

def read_file(file):
    with open(file, 'r') as f:
        # data = f.read().splitlines()
        # grouped = [list(g) for k,g in groupby(data, bool) if k]
        # biggest_sum = max(sum(int(elem) for elem in single_list) for single_list in grouped)
        # print(biggest_sum)

        data = f.read().split('\n\n')
        sums = [sum(map(int, sublist.split())) for sublist in data]
        print(max(sums), sum(sorted(sums[-3:])))

read_file(sys.argv[1])
