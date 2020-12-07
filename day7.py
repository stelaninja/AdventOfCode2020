"""

Solution from Sophie Alpert - https://github.com/sophiebits

Why? Because I went down the rabbit hole. Need to study and practice graphs more.

"""

from collections import defaultdict
import re

X = [x for x in open("input7.in").read().splitlines()]

TestX = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
# X = [x for x in TestX.splitlines()]

in_bag = defaultdict(set)
bag_contains = defaultdict(list)

for x in X:
    bag_color = re.match(r"(.+?) bags contain", x)[1]
    for num_bags, contain_colors in re.findall(r"(\d+) (.+?) bags?[,.]", x):
        in_bag[contain_colors].add(bag_color)
        bag_contains[bag_color].append((int(num_bags), contain_colors))

# part 1:
# print(in_bag)
has_shiny_gold = set()


def find_bag_color(bag_color):
    for c in in_bag[bag_color]:
        has_shiny_gold.add(c)
        find_bag_color(c)


def find_num_of_bags(bag_color):
    total_num = 0
    for num_bags, contain_color in bag_contains[bag_color]:
        total_num += num_bags
        total_num += num_bags * find_num_of_bags(contain_color)

    return total_num


find_bag_color("shiny gold")
print("Part 1:", len(has_shiny_gold))
print("Part 2:", find_num_of_bags("shiny gold"))
