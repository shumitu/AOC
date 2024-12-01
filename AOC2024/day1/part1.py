def calculate(file):
    with open(file, 'r') as f:
        lst = [l.split() for l in f.readlines()]
        left = sorted(int(n[0]) for n in lst)
        right = sorted(int(n[1]) for n in lst)
        diff = sum(map(lambda x: abs(x[0] - x[1]), zip(left, right)))
        print(diff)
        
calculate('data.txt')