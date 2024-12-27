from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return f.read()
    
    
def part12(string, n):
    tmp = string
    for _ in range(n):
        if len(tmp) == 1: 
            tmp = tmp * 2
        else:
            groups = [tmp[0]]
            for i in range(1, len(tmp)):
                if tmp[i - 1] == tmp[i]:
                    groups[-1] += tmp[i]
                else:
                    groups.append(tmp[i])
            
            tmp = ''
            for s in groups:
                tmp += str(len(s)) + s[0]

    return len(tmp)
            

time = timer()
string = load_data('data.txt')
print(f"Part one: {part12(string, 40)}")
print(f"Part two: {part12(string, 50)}")
time2 = timer()
print(f"Execution time: {(time2 - time) * 1000:.3f}ms")