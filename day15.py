from collections import defaultdict, namedtuple, Counter
from copy import deepcopy
import re

X = [x for x in open("input15.in").read().strip().split(",")]


testX = "0,3,6".split(",")


data = testX


spoken = [int(x) for x in data[:-1]]

spoken_time = defaultdict(int)

for i, num in enumerate(data[:-1]):
    spoken_time[int(num)] = i + 1

last_spoken = 3
next_num = 6


for i in range(len(data) + 1, 11):
    last_spoken = next_num
    if next_num not in spoken:
        next_num = 0
    else:
        next_num = i - 1 - spoken_time[next_num]

    print(next_num)

    spoken_time[last_spoken] = i

print(spoken_time)
