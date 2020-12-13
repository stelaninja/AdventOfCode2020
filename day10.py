from collections import defaultdict, namedtuple, Counter
import re

X = [int(x) for x in open("input10.in").read().splitlines()]

testX = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

testX = [int(x) for x in testX.split()]


def find_diffs(jolt1, jolt2, data=X):
    data.sort()
    data.insert(0, 0)
    diff = [data[i] - data[i - 1] for i in range(1, len(data))]
    diff.insert(0, 0)

    return (
        diff.count(jolt1),
        diff.count(jolt2) + 1,
        diff.count(jolt1) * (diff.count(jolt2) + 1),
    )


part1 = find_diffs(1, 3, X)

print(part1[2])
