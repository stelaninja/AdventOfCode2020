from collections import defaultdict, namedtuple, Counter
import re

X = [x for x in open("input13.in").read().splitlines()]

testX = """939
7,13,x,x,59,x,31,19"""

testX = [x for x in testX.splitlines()]

data = X

timestamp = int(data[0])

busses = [int(x) for x in data[1].split(",") if x != "x"]

print(timestamp)
print(busses)


def check_time(timestamp, busses):
    for t in range(timestamp, timestamp + max(busses)):
        for b in busses:
            if t % b == 0:
                wait = t - timestamp
                return t, b, wait


part1 = check_time(timestamp, busses)
print(f"Part 1: Timestamp {part1[0]}, buss {part1[1]}, wait {part1[2]} minutes.")
print(f"Part 1: Answer is {part1[1]* part1[2]}")
