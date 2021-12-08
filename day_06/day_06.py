with open('day_06_input.txt', 'r', encoding='utf-8') as f:
    data_list = f.readline().rstrip().split(',')


def get_dict(data):
    data_dict = {}
    for timer in data:
        if timer not in data_dict.keys():
            data_dict[timer] = 1
        else:
            data_dict[timer] += 1
    return data_dict


def count_fish(data, days):
    for day in range(1, days + 1):
        new_data_dict = {}
        for key, value in data.items():
            if key == '0':
                new_data_dict['8'] = value
                if '6' in new_data_dict:
                    new_data_dict['6'] += value
                else:
                    new_data_dict['6'] = value
            elif str(int(key) - 1) in new_data_dict:
                new_data_dict['6'] += value
            else:
                new_data_dict[str(int(key) - 1)] = value
        data = new_data_dict

    print(sum(data.values()))


if __name__ == '__main__':
    # part 1
    count_fish(get_dict(data_list), 80)
    # part 2
    count_fish(get_dict(data_list), 256)
