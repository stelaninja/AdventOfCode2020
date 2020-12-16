import re

f_name = "input16.in"

with open(f_name, "r") as f:
    line = None
    ticket_info = []
    while line != "your ticket:":
        line = f.readline().strip()
        if line != "":
            ticket_info.append(line)

    while line != "nearby tickets:":
        line = f.readline().strip()
        if line != "" and line != "nearby tickets:":
            my_ticket_info = line.split(",")

    ticket_info.pop()
    nearby_tickets = [x.strip() for x in f.readlines()]

all_rules_valid_nums = set()
rule_dict = {}
rule_tests = {}

for row in ticket_info:
    limits = re.findall(r"\d+-\d+", row)
    rule = re.findall(r"^[a-zA-Z ]+", row)

    rule_valid_nums = []
    for num in limits:
        num = num.split("-")
        low = int(num[0])
        high = int(num[1])
        for i in range(int(low), int(high) + 1):
            all_rules_valid_nums.add(i)
            rule_valid_nums.append(i)

    rule_dict[rule[0]] = rule_valid_nums
    rule_tests[rule[0]] = []


valid = []
invalid = []
valid_tickets = []

for ticket in nearby_tickets:
    test = True
    for num in ticket.split(","):
        if int(num) not in all_rules_valid_nums:
            invalid.append(int(num))
            test = False
        else:
            valid.append(int(num))
    if test:
        valid_tickets.append((ticket))


pos_dict = {}
valid_tickets = [ticket.split(",") for ticket in valid_tickets]

check = 0
for rule in rule_dict.keys():
    for i in range(len(valid_tickets[0])):
        match = 0
        not_match = 0
        num_ticks = 0

        for j, ticket in enumerate(valid_tickets):
            num_ticks += 1
            if int(ticket[i]) in rule_dict[rule]:
                match += 1

            else:
                not_match += 1

        if match == num_ticks:
            rule_tests[rule].append(i)

check_dict = {}
used_pos = set()

possible = [x for x in range(20)]
empty_lists = len(rule_tests.keys())

while len(rule_tests) > 0:
    for rule in list(rule_tests.keys()):
        if len(rule_tests[rule]) == 1 and rule_tests[rule][0] not in used_pos:
            check_dict[rule] = rule_tests[rule].pop()
            used_pos.add(check_dict[rule])
            del rule_tests[rule]
            # print(rule)
        else:
            for poss in used_pos:
                if poss in rule_tests[rule]:
                    rule_tests[rule].remove(poss)


factor = 1

for key, value in check_dict.items():
    if key.startswith("departure"):
        factor *= int(my_ticket_info[value])
        print(my_ticket_info[value])

print(f"Part 1: {sum(invalid)}")
print(f"Part 2: {factor}")
