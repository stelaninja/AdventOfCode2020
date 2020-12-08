"""
Part to solved with a bit of help from watching Jonathan Paulson - https://www.youtube.com/watch?v=ZSGTr55gmIs
"""

from collections import defaultdict, namedtuple, Counter
import re

X = [x for x in open("input8.in").read().splitlines()]


def run_code(X, part):
    acc = 0
    idx_used = []
    i = 0
    last_i = 0

    while 0 <= i < len(X):
        x = X[i].split()

        if i in idx_used:
            if part == 2:
                return False
            else:
                return acc

        inst, val = x[0], int(x[1])

        idx_used.append(i)

        if inst == "nop":
            i += 1

        elif inst == "jmp":
            last_i = i
            i += val

        elif inst == "acc":
            acc += val
            i += 1

        last_i = i

        if i == len(X):
            return acc


def fix_code(X):
    for line in range(len(X)):
        P = list(X)
        if P[line].split()[0] == "jmp":
            P[line] = "nop " + P[line].split()[1]
        elif P[line].split()[0] == "nop":
            P[line] = "jmp " + P[line].split()[1]
        else:
            continue

        try:
            p2 = run_code(P, 2)
        except Exception as e:
            print(e)

        if p2:
            return p2


print("Part 1:", run_code(X, 1))

print("Part 2:", fix_code(X))

