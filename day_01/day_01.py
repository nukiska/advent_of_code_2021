input_list = []
with open('day_01_input.txt', encoding='utf-8') as f:
    for line in f:
        input_list.append(int(line.rstrip()))


def count_increase(data) -> int:
    increased = 0
    previous_value = data[0]

    for i in range(len(data)):
        if data[i] > previous_value:
            increased += 1
        previous_value = data[i]
    return increased


def get_triplets(data) -> list:
    data_list = []
    try:
        for i in range(len(data)):
            data_list.append(data[i] + data[i + 1] + data[i + 2])
    except IndexError:
        return data_list


if __name__ == '__main__':
    # task 1
    print(count_increase(input_list))
    # task 2
    triplets_list = get_triplets(input_list)
    print(count_increase(triplets_list))
