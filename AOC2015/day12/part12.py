import json

def load_data(file):
    with open(file, "r") as f:
        return json.load(f)

    
def handle_list(lst, skip = False):
    sum = 0
    for val in lst:
        if type(val) == dict:
            sum += handle_dict(val, skip)
        elif type(val) == list:
            sum += handle_list(val, skip)
        elif type(val) == int:
            sum += val
    return sum


def handle_dict(dct, skip = False):
    sum = 0
    for val in dct.values():
        if skip and type(val) == str and val == "red":
            sum = 0
            break
        elif type(val) == dict:
            sum += handle_dict(val, skip)
        elif type(val) == list:
            sum += handle_list(val, skip)
        elif type(val) == int:
            sum += val
        
    return sum


def part12(data, skip = False):
    sum = 0
    if type(data) == dict:
        sum += handle_dict(data, skip)
    elif type(data) == list:
        sum += handle_list(data, skip)
    elif type(data) == int:
        sum += data
        
    return sum
    
data = load_data('/mnt/c/Users/darkd/Documents/GitHub/AOC/AOC2015/day12/data.json')

print(f"Part one: {part12(data)}")
print(f"Part two: {part12(data, True)}")