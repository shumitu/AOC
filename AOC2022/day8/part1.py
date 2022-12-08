import sys


def parse_trees(file):
    inside_trees = 0
    with open(file, 'r') as f:
        trees = f.read().splitlines()
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            # check left side
            if int(trees[i][j]) > max(int(x) for x in trees[i][:j]):
                inside_trees += 1
            # check right side
            elif int(trees[i][j]) > max(int(x) for x in trees[i][j+1:]):
                inside_trees += 1
            # check up side
            elif int(trees[i][j]) > max([int(x) for row in range(i) for x in trees[row][j]]):
                inside_trees += 1
            # check down side
            elif int(trees[i][j]) > max([int(x) for row in range(i+1, len(trees)) for x in trees[row][j]]):
                inside_trees += 1
    print(f'Number of all visible trees: {inside_trees + 2*len(trees) + 2*len(trees[0]) - 4}')

    list_of_scores = []
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            left, up, right, down = 0, 0, 0, 0
            # check left side
            for elem in [int(x) for x in trees[i][:j]][::-1]:
                if elem >= int(trees[i][j]):
                    left += 1
                    break
                elif elem < int(trees[i][j]):
                    left += 1

            # check right side
            for elem in [int(x) for x in trees[i][j+1:]]:
                if elem >= int(trees[i][j]):
                    right += 1
                    break
                elif elem < int(trees[i][j]):
                    right += 1

            # check up side
            for elem in [int(x) for row in range(i) for x in trees[row][j]][::-1]:
                if elem >= int(trees[i][j]):
                    up += 1
                    break
                elif elem < int(trees[i][j]):
                    up += 1

            # check down side
            for elem in [int(x) for row in range(i+1, len(trees)) for x in trees[row][j]]:
                if elem >= int(trees[i][j]):
                    down += 1
                    break
                elif elem < int(trees[i][j]):
                    down += 1

            list_of_scores.append(left*right*down*up)

    print(f'Max score for tree is: {max(list_of_scores)}')


if __name__ == '__main__':
    parse_trees(sys.argv[1])
