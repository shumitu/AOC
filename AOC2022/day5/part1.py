import sys
import numpy as np

def do_crane_work(file):
    with open(file, 'r') as f:
        data = f.read().split('\n\n')
        steps = [line for line in data[1]]
        
        arr_raw = [row.replace(' ', '.') for row in data[0].splitlines()[:-1]]
        arr_plain_letters = [[e.replace('[', '.').replace(']', '.') for e in row] for row in arr_raw]
        arr = np.array(arr_plain_letters)
        arr4 = arr[:, 1::2]

        print(arr4)

if __name__ == '__main__':
    do_crane_work(sys.argv[1])