import sys
from collections import Counter


def calculate(file):
    data = []
    with open(file) as f:
        data = f.read().splitlines()
    filtered_data_oxygen = [[] for _ in range(len(data[0]))]
    filtered_data_co2 = [[] for _ in range(len(data[0]))]
    filtered_data_oxygen[0] = list(filter(lambda x: x[0] == Counter(
        sorted([x[0] for x in data], reverse=True)).most_common()[0][0], data))
    filtered_data_co2[0] = list(filter(lambda x: x[0] == Counter(
        sorted([x[0] for x in data], reverse=True)).most_common()[-1][0], data))

    for i in range(1, len(data[0])):
        filtered_data_oxygen[i] = list(filter(lambda x: x[i] == Counter(sorted(
            [x[i] for x in filtered_data_oxygen[i - 1]], reverse=True)).most_common()[0][0], filtered_data_oxygen[i - 1]))
        filtered_data_co2[i] = list(filter(lambda x: x[i] == Counter(sorted(
            [x[i] for x in filtered_data_co2[i - 1]], reverse=True)).most_common()[-1][0], filtered_data_co2[i - 1]))
    final_oxygen = int(filtered_data_oxygen[-1][0], 2)
    final_co2 = int(filtered_data_co2[-1][0], 2)

    print(final_oxygen, final_co2, final_oxygen * final_co2)


if __name__ == '__main__':
    calculate(sys.argv[1])
