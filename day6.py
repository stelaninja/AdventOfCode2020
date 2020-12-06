X = [x for x in open("input6.in").read().split("\n\n")]
Y = [y.split() for y in X]


def get_group_answers(group):
    answer_list = []
    answer_dict = {}
    answer2 = 0

    for person in group:
        for ans in person:
            if ans not in answer_dict:
                answer_dict[ans] = 1
            else:
                answer_dict[ans] += 1

            answer_list.append(ans)

    for key in answer_dict:
        if answer_dict[key] == len(group):
            answer2 += 1

    answer1 = set(answer_list)

    return len(answer1), answer2


p1 = p2 = 0

for group in Y:
    answer1, answer2 = get_group_answers(group)
    p1 += answer1
    p2 += answer2


print("Part 1:", p1)
print("Part 2:", p2)
