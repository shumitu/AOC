def load_data(file):
    with open(file, 'r') as f:
        return f.read().splitlines()
    
    
def part1(strings):
    nice_strings = 0
    vowels = 'aeiou'
    not_allowed = ['ab', 'cd', 'pq', 'xy']
    for string in strings:
        vowels_num, doubles_num = 0, 0
        for c in string:
            if c in vowels:
                vowels_num += 1
        for c in zip(string, string[1:]):
            if c[0] == c[1]: doubles_num += 1
        if vowels_num >= 3 and doubles_num >= 1 and not any(s in string for s in not_allowed):
            nice_strings += 1
    return nice_strings


def part2(strings):
    nice_strings = 0
    for string in strings:
        repeated, pairs = 0, 0
        for triple in zip(string, string[1:], string[2:]):
            if triple[0] == triple[2]: repeated += 1
        for i in range(len(string) - 2):
            s = string[i:i+2]
            # print(string[:i], s, string[i+2:])
            if s in string[:i] or s in string[i+2:]:
                pairs += 1  
            
        if repeated > 0 and pairs > 0: 
            nice_strings += 1
          
    return nice_strings
            


strings = load_data('/mnt/c/Users/darkd/Documents/GitHub/AOC/AOC2015/day5/data.txt')
part1(strings)
print(f"Part one: {part1(strings)}")
print(f"Part two: {part2(strings)}")

