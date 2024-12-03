import re

def load_data(file):
    with open(file, 'r') as f:
        return f.read()
    

def parse_part1(data):
    main_rgx = r'mul\(\d+,\d+\)'
    findings = re.findall(main_rgx, data)
    sum = 0
    for s in findings:
        num1, num2 = map(int, s.strip('mul()').split(','))
        sum += num1 * num2
    return sum


def parse_part2(data):
    cond_rgx = r'(don\'t\(\)|do\(\))'
    findings = re.split(cond_rgx, data)
    sum = 0 
    process = True
    for s in findings:
        if s == "don't()":
            process = False
        elif s == "do()":
            process = True
        if process:
            sum += parse_part1(s)
    return sum    

data = load_data('data.txt')
print(f"Sum for part1: {parse_part1(data)}")
print(f"Sum for part2: {parse_part2(data)}")