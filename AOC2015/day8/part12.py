def load_data(file):
    with open(file, 'r') as f:
        return [l for l in f.read().splitlines()]
    

def check_str(string):
    char_sum, string_sum = len(string), len(string) - 2
    i = 1
    while i < len(string):
        if string[i] == '\\':
            if string[i + 1] == 'x':
                string_sum -= 3
                i += 3  
            else:
                string_sum -= 1
                i += 1
        i += 1

    return char_sum - string_sum 


def check_str2(string):
    char_sum, string_sum = len(string), 2
    i = 0
    while i < len(string):
        if string[i] == '"':
            string_sum += 2
        elif string[i] == '\\':
            if string[i + 1] == 'x':
                string_sum += 5
                i += 3  
            else:
                string_sum += 4
                i += 1
        else: string_sum += 1
        i += 1

    return string_sum - char_sum

        
def part1(data):
    return sum(check_str(s) for s in data)


def part2(data):
    return sum(check_str2(s) for s in data)



data = load_data('data.txt')
print(f"Part one: {part1(data)}")
print(f"Part two: {part2(data)}")
