input_list = []
with open('day_10_input.txt', encoding='utf-8') as f:
    for line in f:
        input_list.append(list(line.rstrip()))

open_brackets = ('(', '[', '{', '<')
closed_brackets = (')', ']', '}', '>')

error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def count_total_error_score(data) -> int:
    total_score = 0
    rank = []
    for data_line in data:
        for bracket in data_line:
            if bracket in open_brackets:
                rank.append(bracket)
            elif bracket in closed_brackets:
                last_open_bracket = rank.pop()
                if open_brackets.index(last_open_bracket) == closed_brackets.index(bracket):
                    continue
                else:
                    total_score += error_scores[bracket]
    return total_score


complete_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def count_middle_score(data) -> int:
    score_list = []
    for data_line in data:
        rank = []
        line_score = 0
        for bracket in data_line:
            if bracket in open_brackets:
                rank.append(bracket)
            elif bracket in closed_brackets:
                if open_brackets.index(rank[-1]) == closed_brackets.index(bracket):
                    del rank[-1]
                    continue
                else:
                    rank = []
                    break
        if len(rank) > 0:
            for bracket in reversed(rank):
                line_score = line_score * 5 + complete_scores[bracket]
            score_list.append(line_score)
    score_list.sort()
    middle_score = score_list[(len(score_list) // 2)]
    return middle_score


if __name__ == '__main__':
    # part 1
    print(count_total_error_score(input_list))
    # part 2
    print(count_middle_score(input_list))
