with open('day_07_input.txt', 'r', encoding='utf-8') as f:
    data_list = f.readline().rstrip().split(',')

    data_dict = {}
    for d in data_list:
        if int(d) not in data_dict.keys():
            data_dict[int(d)] = 1
        else:
            data_dict[int(d)] += 1


def count_min_fuel(data: dict):
    fuel_list = []
    for position in data_dict.keys():
        fuel = 0
        for key, value in data.items():
            fuel += abs((int(key) - position) * value)
        fuel_list.append(fuel)
    return min(fuel_list)


def count_min_fuel_gradual(data: dict):
    fuel_list_gradual = []
    for position in range(min(data_dict.keys()), max(data_dict.keys())):
        fuel = 0
        for key, value in data.items():
            differential = abs(int(key) - position)
            gradual = ((differential + 1) / 2) * differential
            fuel += gradual * value
        fuel_list_gradual.append(fuel)
    return int(min(fuel_list_gradual))


if __name__ == '__main__':
    # task 1
    print(count_min_fuel(data_dict))
    # task 2
    print(count_min_fuel_gradual(data_dict))
