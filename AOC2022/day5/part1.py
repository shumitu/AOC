import sys
import numpy as np

def do_crane_work(file):
    with open(file, 'r') as f:
        data = f.read().split('\n\n')
        steps_raw = [line for line in data[1].splitlines()]
        steps_numbers = [[int(n) for n in row.split() if n.isdigit()] for row in steps_raw]

        arr_raw = [row.replace(' ', '.') for row in data[0].splitlines()[:-1]]
        arr_plain_letters = [[e.replace('[', '.').replace(']', '.') for e in row] for row in arr_raw]
        temp_arr_numpy = np.array(arr_plain_letters)
        temp_arr_numpy_1 = temp_arr_numpy[:, 1::2]
        temp_arr_numpy_2 = temp_arr_numpy_1[:, 0::2]
        transposed_array = np.transpose(temp_arr_numpy_2)
        cleaned_array = [[l for l in row if l != '.'] for row in transposed_array.tolist()]
        cleaned_reversed_array = [row[::-1] for row in cleaned_array]

        max_of_columns = max([max(triple) for triple in steps_numbers])
        cleaned_reversed_array.extend([] for _ in range(max_of_columns - len(cleaned_reversed_array))) 
        
        for count, source, target in steps_numbers:

            values = cleaned_reversed_array[source - 1][- count:]
            del cleaned_reversed_array[source - 1][- count:]
            # for part 1
            cleaned_reversed_array[target -1].extend(values[::-1])
            # for part 2
            # cleaned_reversed_array[target -1].extend(values)
        
        print(''.join(l[-1] for l in cleaned_reversed_array if l))

if __name__ == '__main__':
    do_crane_work(sys.argv[1])