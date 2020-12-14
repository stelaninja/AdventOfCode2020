from collections import defaultdict, namedtuple, Counter
from copy import deepcopy
import re

X = [x for x in open("input14.in").read().splitlines()]

testX = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

testX2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

testX = [x for x in testX.splitlines()]
testX2 = [x for x in testX2.splitlines()]

data = X

# print(data)
mask = ""
temp = 0


def update_mem(mem, mem_loc, value, mask):
    value = list(f"{int(value):b}".zfill(36))
    new_bits = list(mask)

    for i in range(len(mask)):
        if new_bits[i] == "X":
            new_bits[i] = value[i]
        else:
            pass
    # print(mem_loc, value, mask)
    # print("".join(new_bits))
    mem[mem_loc] = int("".join(new_bits), 2)
    return mem


def decode_mem(mem, mem_loc, value, mask):
    value = list(f"{int(value):b}".zfill(36))
    adress = list(f"{int(mem_loc):b}".zfill(36))
    new_bits = [x for x in mask]
    temp = 0
    combo_list = []

    for i in range(len(mask)):
        if new_bits[i] == "X":
            continue
        elif new_bits[i] == "0":
            new_bits[i] = adress[i]
        elif new_bits[i] == "1":
            new_bits[i] = "1"

    combo = "".join(new_bits)
    all_combinations(list(combo), combo_list)
    for j in combo_list:
        mem[j] = int("".join(value), 2)
    return mem


def all_combinations(combo, combo_list, i=0):
    opts = "01"

    if i == len(combo):
        # print("".join(combo), int("".join(combo), 2))
        combo_list.append(int("".join(combo), 2))
        return

    if combo[i] == "X":
        for c in opts:
            combo[i] = c

            all_combinations(combo, combo_list, i + 1)

            combo[i] = "X"

    else:
        all_combinations(combo, combo_list, i + 1)

    return


def part1(data=data):
    mem = {}
    for row in data:
        if row[:4] == "mask":
            mask = row[7:]

        else:
            mem_data = row.split()
            mem_loc = re.findall(r"\[(\d+)\]", mem_data[0])
            value = mem_data[2]

            update_mem(mem, mem_loc[0], value, mask)
    return mem


def part2(data=data):
    mem = {}
    temp = 0
    for row in data:
        if row[:4] == "mask":
            mask = row[7:]

        else:
            mem_data = row.split()
            mem_loc = re.findall(r"\[(\d+)\]", mem_data[0])
            value = mem_data[2]

            decode_mem(mem, mem_loc[0], value, mask)
    return mem


p1_mem = part1()

p2_mem = part2()
print(f"Part 1: {sum(p1_mem.values())}")
print(f"Part 2: {sum(p2_mem.values())}")

