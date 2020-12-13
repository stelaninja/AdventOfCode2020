from collections import defaultdict, namedtuple, Counter
from copy import deepcopy
import re

with open("input11.in", "r") as f:
    X = f.read().strip()

X = [x for x in X.strip().split()]
X = [[x for x in y] for y in X]


testX = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


# testX = [x for x in testX.split()]
# testX = [[x for x in y] for y in testX]


class Board:
    def __init__(self, data):
        self.data = data
        self.empty_list = [[0 for x in data] for data in data]
        self.row_len = len(data)
        self.col_len = len(data[0])
        self.control_data = []

    def check_right(self, row, col, char):
        if self.data[row][col + 1] == char:
            return 1
        else:
            return 0

    def check_left(self, row, col, char):
        if self.data[row][col - 1] == char:
            return 1
        else:
            return 0

    def check_up(self, row, col, char):
        if self.data[row - 1][col] == char:
            return 1
        else:
            return 0

    def check_down(self, row, col, char):
        if self.data[row + 1][col] == char:
            return 1
        else:
            return 0

    def check_up_right(self, row, col, char):
        if self.data[row - 1][col + 1] == char:
            return 1
        else:
            return 0

    def check_up_left(self, row, col, char):
        if self.data[row - 1][col - 1] == char:
            return 1
        else:
            return 0

    def check_down_right(self, row, col, char):
        if self.data[row + 1][col + 1] == char:
            return 1
        else:
            return 0

    def check_down_left(self, row, col, char):
        if self.data[row + 1][col - 1] == char:
            return 1
        else:
            return 0

    def check(self, row, col, char):
        num_adj = 0
        if 0 < row < self.row_len - 1 and 0 < col < self.col_len - 1:
            num_adj += self.check_left(row, col, char)
            num_adj += self.check_right(row, col, char)
            num_adj += self.check_up(row, col, char)
            num_adj += self.check_down(row, col, char)
            num_adj += self.check_up_left(row, col, char)
            num_adj += self.check_up_right(row, col, char)
            num_adj += self.check_down_left(row, col, char)
            num_adj += self.check_down_right(row, col, char)

        elif row == 0:
            num_adj += self.check_down(row, col, char)
            if 0 < col < self.col_len - 1:
                num_adj += self.check_right(row, col, char)
                num_adj += self.check_left(row, col, char)
                num_adj += self.check_down_left(row, col, char)
                num_adj += self.check_down_right(row, col, char)
            elif col == self.col_len - 1:
                num_adj += self.check_left(row, col, char)
                num_adj += self.check_down_left(row, col, char)

        elif row == self.row_len - 1:
            num_adj += self.check_up(row, col, char)
            if 0 < col < self.col_len - 1:
                num_adj += self.check_right(row, col, char)
                num_adj += self.check_left(row, col, char)
                num_adj += self.check_up_left(row, col, char)
                num_adj += self.check_up_right(row, col, char)
            elif col == self.col_len - 1:
                num_adj += self.check_left(row, col, char)
                num_adj += self.check_up_left(row, col, char)

        elif row == self.row_len - 1 and 0 < col < self.col_len - 1:
            num_adj += self.check_right(row, col, char)
            num_adj += self.check_left(row, col, char)
            num_adj += self.check_up(row, col, char)
            num_adj += self.check_up_left(row, col, char)
            num_adj += self.check_up_right(row, col, char)

        elif 0 < row < self.row_len - 1 and col == self.col_len - 1:
            num_adj += self.check_left(row, col, char)
            num_adj += self.check_up(row, col, char)
            num_adj += self.check_down(row, col, char)
            num_adj += self.check_up_left(row, col, char)
            num_adj += self.check_down_left(row, col, char)

        elif 0 < row < self.row_len - 1 and col == 0:
            num_adj += self.check_right(row, col, char)
            num_adj += self.check_up(row, col, char)
            num_adj += self.check_down(row, col, char)
            num_adj += self.check_up_right(row, col, char)
            num_adj += self.check_down_right(row, col, char)

        if self.data[row][col] == ".":
            self.empty_list[row][col] = "."
        else:
            self.empty_list[row][col] = num_adj

    def get_adjacent_seats(self):
        for row in range(self.row_len):
            for col in range(self.col_len):
                self.check(row, col, "#")

    def run_rule(self, acceptance=4):
        stabilized = True
        for row in range(self.row_len):
            for col in range(self.col_len):
                if self.data[row][col] == "L" and self.empty_list[row][col] == 0:
                    self.data[row][col] = "#"
                elif (
                    self.data[row][col] == "#"
                    and self.empty_list[row][col] >= acceptance
                ):
                    self.data[row][col] = "L"

        if self.data == self.control_data:
            stabilized = True
        else:
            stabilized = False

        if stabilized == True:

            num_seated = 0
            for row in self.data:
                num_seated += row.count("#")
            print(f"\n\nStabilized at {num_seated}")
            stop_run()

        self.control_data = deepcopy(self.data)


def stop_run():
    exit()


board = Board(X)
run = True


def part1(acc=4):
    while run:
        board.get_adjacent_seats()
        board.run_rule(acceptance=acc)


part1()
