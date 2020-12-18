"""

Solution to part 1 from Luke Storry - https://github.com/LukeStorry

I need to learn more about the Regex methods better. How they work and what they return.

"""

import re

X = [x.replace(" ", "") for x in open("input18.in").readlines()]

testX = """2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

testX = [x.strip().replace(" ", "") for x in testX.split("\n")]

data = testX


re_parent = re.compile(r"\((\d+)\)")
re_expr = re.compile(r"(\d+)([+*])(\d+)")


def calc_expr(expr_str):
    expr = re_expr.search(expr_str)
    while expr is not None:
        first, oper, scnd = expr.groups()

        if oper == "+":
            new = int(first) + int(scnd)
        else:
            new = int(first) * int(scnd)

        expr_str = expr_str[: expr.start()] + str(new) + expr_str[expr.end() :]
        expr_str = re_parent.sub(r"\1", expr_str)
        expr = re_expr.search(expr_str)

    return int(expr_str)


part1 = 0
for expr in data:
    print(expr)
    part1 += calc_expr(expr)
    print(calc_expr(expr))
    print("-" * 40)

print(f"Part 1:", part1)
