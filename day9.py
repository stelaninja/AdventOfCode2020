from collections import defaultdict, namedtuple, Counter
import re

X = [int(x) for x in open("input9.in").read().splitlines()]

testX = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

testX = [int(x) for x in testX.splitlines()]


def sums_to_index(index, preamble=25, data=X):
    used_nums = set()
    for x in data[index - preamble : index]:
        for y in data[index - preamble : index]:
            if x + y == data[index] and x != y and x + y not in used_nums:
                used_nums.update([x, y])
                return True, x, y, data[index]
    return False, data[index]


def find_encryption_weakness(num, data=X):
    for i, x in enumerate(data):
        for y in range(i, len(data)):
            summ = sum(data[i:y])
            if summ == num:
                return True, min(data[i:y]) + max(data[i:y])


for i in range(25, len(X)):
    part1 = sums_to_index(i)
    if part1[0] == False:
        print(f"Part 1: {part1}")
        break

part2 = find_encryption_weakness(part1[1], X)
print(f"Part 2: {part2}")

