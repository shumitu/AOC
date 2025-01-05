from timeit import default_timer as timer
from math import sqrt

def load_data(file):
    with open(file, "r") as f:
        return f.read()
    

def get_divisors(n):
    lst = []
    i = 1
    while i < sqrt(n):
        if n % i == 0:
            lst.append(i)
            if (d:= n // i) != i:
                lst.append(d)
        i += 1
        
    return lst


def part1(val):
    house = 1
    while True:
            
        if sum(d * 10 for d in get_divisors(house)) >= val:
            return house
        
        house += 1

        
def part2(val):
    house = 1
    while True:
            
        if sum(d * 11 if house // d <= 50 else 0 for d in get_divisors(house)) >= val:
            return house
        
        house += 1


time = timer()
val = int(load_data("data.txt"))
print(f"Part one: {part1(33100000)}")
print(f"Part two: {part2(33100000)}")
time2 = timer()
print(f"Execution time: {(time2-time):.2f}s")