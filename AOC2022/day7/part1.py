import sys

def load_data(file):
    with open(file, 'r') as f:
        return f.read().splitlines()

def go_up(dirs_sizes, subdirs_sizes):
    subdirs_sizes.append(dirs_sizes.pop(-1))
    if dirs_sizes:
        dirs_sizes[-1] += subdirs_sizes[-1]

def parse_tree(commands_list):
    dirs_sizes, subdirs_sizes = [], []
    for command in commands_list:
        match command.split():
            case "$", "cd", "..": go_up(dirs_sizes, subdirs_sizes)
            case "$", "cd", _: dirs_sizes.append(0)
            case ("$", _) | ("dir", _): pass
            case size, _: dirs_sizes[-1] += int(size)

    while dirs_sizes:
        go_up(dirs_sizes, subdirs_sizes)

    print(f'Part one size is: {sum(s for s in subdirs_sizes if s <= 100000)}')
    print(f'Part two size is: {min(s for s in subdirs_sizes if s >= max(subdirs_sizes) - 40000000)}')

if __name__ == '__main__':
    list_of_commands = load_data(sys.argv[1])
    parse_tree(list_of_commands)