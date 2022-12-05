import sys

def do_crane_work(file):
    with open(file, 'r') as f:
        data = f.read().split('\n\n')
        steps_raw = [line for line in data[1].splitlines()]
        steps_numbers = [[int(n) for n in row.split() if n.isdigit()] for row in steps_raw]

        arr_raw = [row[1::4] for row in data[0].splitlines()[:-1]]
        arr_transposed = [[l[i] for l in arr_raw if l[i] != ' '][::-1] for i in range(len(arr_raw[0]))]

        map_of_array = {k:v for k,v in enumerate(arr_transposed)}
        
        for count, source, target in steps_numbers:

            values = map_of_array[source - 1][- count:]
            del map_of_array[source - 1][- count:]
            # for part 1
            # if target - 1 in map_of_array:
            #     map_of_array[target - 1].extend(values[::-1])
            # else: 
            #     map_of_array[target - 1] = values[::-1]
            # for part 2
            if target - 1 in map_of_array:
                map_of_array[target - 1].extend(values)
            else: 
                map_of_array[target - 1] = values

        print(''.join(l[-1] for l in map_of_array.values() if l))

if __name__ == '__main__':
    do_crane_work(sys.argv[1])