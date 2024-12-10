from collections import deque
from timeit import default_timer as timer

def load_data(file):
    with open(file, 'r') as f:
        return f.read()

def part1(data):
    data_list = deque()
    final_list = deque()        
    
    counter = 0
    for i in range(len(data)):
        if i % 2 == 0:
            data_list.extend([counter] * int(data[i]))
            counter += 1
        else:
            data_list.extend(['.'] * int(data[i]))

    lst_range, i = len(data_list), 0

    while i < lst_range:
        if data_list[i] != '.':
            final_list.append(data_list[i])
        else:
            while right_item := data_list.pop():
                lst_range -= 1
                if right_item != '.':
                    final_list.append(right_item)
                    break
        i += 1
            
    return sum(a * b for a, b in enumerate(final_list))


def part2(data):
    data_list = deque()
    counter = 0
    for i in range(len(data)):
        if i % 2 == 0:
            data_list.append((counter, tuple((counter,) * int(data[i]))))
            counter += 1
        else:
            if int(data[i]) > 0:
                data_list.append(('.', tuple(('.',) * int(data[i]))))
    
    moved_or_checked = set()
    temp_left, temp_right = deque(), deque()
        
    while len(data_list) > 0 and (right_item := data_list.pop()):
        right_item_added = False
        temp_left = deque()
        pop_left, pop_right = 0, 0
        if right_item[0] == '.':
            temp_right.appendleft(right_item)
        elif right_item[0] != '.' and right_item not in moved_or_checked:
            moved_or_checked.add(right_item)
            for i, left_item in enumerate(data_list):
                if left_item[0] != '.':
                    temp_left.append(left_item)
                    pop_left += 1
                    
                else:
                    left_item_length, right_item_length = len(left_item[1]), len(right_item[1])
                    if left_item_length >= right_item_length:
                        temp_left.append(right_item)
                        right_item_added = True
                        pop_left += 1
                        if left_item_length > right_item_length:
                            additional_item = ('.',  tuple('.' for _ in range(left_item_length - right_item_length)))
                            temp_left.append(additional_item)
                        temp_right.appendleft(('.',  tuple('.' for _ in range(right_item_length))))
                        break
                    elif left_item_length < right_item_length:
                        temp_left.append(left_item)
                        pop_left += 1
                        continue

            if not right_item_added: 
                temp_right.appendleft(right_item)
                
        elif right_item[0] != '.' and right_item in moved_or_checked:
            temp = temp_right.popleft()
            if right_item != temp:
                temp_right.appendleft(temp)
                temp_right.appendleft(right_item)
            else:
                temp_right.appendleft(temp)
        
        if right_item_added:
            for _ in range(pop_left):
                data_list.popleft()
            if pop_left > 0:
                for _ in range(len(temp_left)):
                    data_list.appendleft(temp_left.pop())

    sum = 0
    final_list = []
    for item in temp_right:
        final_list.extend([*item[1]])
        
    for i, item in enumerate(final_list):
        sum += i * item if isinstance(item, int) else 0

    return sum

time1 = timer()
data = load_data('data.txt')
time2 = timer()
print(f"Data load time: {(time2 - time1) * 1000:.3f}ms")
print(f"Part one: {part1(data)}")
time3 = timer()
print(f"Part one execution time: {(time3 - time2) * 1000:.3f}ms")
print(f"Part two: {part2(data)}")
time4 = timer()
print(f"Part two execution time: {(time4 - time3) * 1000:.3f}ms")


