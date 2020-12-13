from collections import defaultdict, namedtuple, Counter
import re

X = [x for x in open("input12.in").read().splitlines()]

testX = """F10
N3
F7
R90
F11
L90
F1
L90
F10"""

# X = [x for x in testX.splitlines()]
print(X)

x_pos = 0
y_pos = 0
direction = 0

for line in X:
    action = line[0]
    val = line[1:]

    print(action, val, x_pos, y_pos)

    if action == "N":
        y_pos += int(val)

    elif action == "S":
        y_pos -= int(val)

    elif action == "W":
        x_pos -= int(val)

    elif action == "E":
        x_pos += int(val)

    elif action == "F":
        if direction == 0:
            x_pos += int(val)
        elif direction == 1:
            y_pos -= int(val)
        elif direction == 2:
            x_pos -= int(val)
        elif direction == 3:
            y_pos += int(val)

    elif action == "R":
        turn = int(val) // 90
        direction = (direction + turn) % 4
        print(turn, direction)

    elif action == "L":
        turn = int(val) // 90
        direction = (direction - turn) % 4
        print(turn, direction)

print(x_pos, y_pos)
print(abs(x_pos) + abs(y_pos))
