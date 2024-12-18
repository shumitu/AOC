import hashlib
from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return f.read()
    

def part12(s, n):
    i = 0
    while True:
        test = s + str(i)
        if hashlib.md5(test.encode()).hexdigest()[:n] == "0" * n:
            return i
        i += 1
    

time = timer()
string = load_data('data.txt')
print(f"Part one: {part12(string, 5)}")
print(f"Part two: {part12(string, 6)}")
time2 = timer()
print(f"Execution time: {(time2 - time):.3f}s")