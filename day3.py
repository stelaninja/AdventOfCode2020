X = [x for x in open("input3.in").read().splitlines()]

tree_map = [line for line in X]


def slope_traverse(tree_map, down=1, right=3):
    num_trees = 0
    num_open = 0
    j = 0
    for i in range(0, len(tree_map), down):
        # print(i, j)
        if tree_map[i][j] == "#":
            num_trees += 1
        else:
            num_open += 1

        j += right
        if j > len(tree_map[0]) - 1:
            j -= len(tree_map[0])
            # print("j:", j)

    return num_trees, num_open


# Part 1
t, o = slope_traverse(tree_map)

print(f"Part 1: {t} trees.")

# Part 2
down_list = [1, 1, 1, 1, 2]
right_list = [1, 3, 5, 7, 1]

t_total = 1
o_total = 1

for index, cur in enumerate(down_list):
    t, o = slope_traverse(tree_map, down=down_list[index], right=right_list[index])
    t_total *= t
    o_total *= o

print(f"Part 2: {t_total} trees.")
