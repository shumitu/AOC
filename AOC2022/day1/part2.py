import sys
from itertools import groupby

def read_file(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
        grouped = [list(g) for k,g in groupby(data, bool) if k]
        sorted_list = sorted([sum(int(elem) for elem in single_list) for single_list in grouped])
        print(sorted_list[-1] + sorted_list[-2] + sorted_list[-3])

read_file(sys.argv[1])
