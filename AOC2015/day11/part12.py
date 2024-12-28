def load_data(file):
    with open(file, 'r') as f:
        return f.read()
    
    
def is_valid(password):
    triples, not_banned_chars, pairs = False, True, False
    # First rule
    for t in zip(password, password[1:], password[2:]):
        if ord(t[1]) - ord(t[0]) == 1 and ord(t[2]) - ord(t[1]) == 1:
            triples = True
    # Second rule
    if any(l in password for l in ['i', 'o', 'l']):
        not_banned_chars = False
    # Third rule
    tmp = [password[0]]
    for i in range(1, len(password)):
        if password[i - 1] == password[i]:
            tmp[-1] += password[i]
        else: 
            tmp.append(password[i])
    pairs_list = [elem for elem in tmp if len(elem) >= 2]
    if len(set(pairs_list)) >= 2:
        pairs = True
    
    return triples and not_banned_chars and pairs
            

def wrap(old_pass, new_pass):    
    # for i in range(len(new_pass) - 1, -1, -1):
    for i in reversed(range(len(new_pass))):
        if new_pass[i] == 'z':
            new_pass = f"{new_pass[:i]}a{new_pass[i+1:]}"
            continue
        else:
            char = chr(ord(new_pass[i])+1)
            new_pass = f"{new_pass[:i]}{char}{new_pass[i+1:]}"
            break

    return old_pass, new_pass
    
    
def part12(password, part):
    if part == 1:
        new_pass, old_pass = password, password
    elif part == 2:
         old_pass, new_pass = wrap(password, password)
    if is_valid(new_pass): 
        return new_pass
    else:
        while not is_valid(new_pass):
            old_pass, new_pass = wrap(old_pass, new_pass)

    return new_pass
    
password = load_data('data.txt')
pwd = part12(password, 1)
print(f"Part one: {pwd}")
print(f"Part two: {part12(pwd, 2)}")