"""

Solution mostly from Sophie Alpert - https://github.com/sophiebits

I was on the right track for part 1 but my Regex knowledge and recursion
skills weren't good enough for me to get the intended result.

Haven't fully understood part 2.

"""

import re

with open("input19.in", "r") as f:
    rules, messages = f.read().strip().split("\n\n")

testX = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

rules, messages = testX.split("\n\n")

# print(rules)

rules = sorted([x for x in rules.splitlines()])
messages = [x for x in messages.splitlines()]

rule_dict = {}
for rule in rules:
    key = re.findall(r"(\d+):", rule)[0]
    val = re.findall(r": (.+)$", rule)[0].split()
    # print(key, val)
    rule_dict[int(key)] = val

rule_dict[8] = "42 | 42 8"
rule_dict[11] = "42 31 | 42 11 31"

print(rule_dict)


def check_rule(rulenum):

    rule = " ".join(rule_dict[rulenum])

    if re.fullmatch(r'"[ab]"', rule):
        return rule.replace('"', "")

    else:
        opts = rule.split(" | ")
        result = []
        for opt in opts:
            rule_nums = opt.split(" ")
            result.append("".join([check_rule(int(r)) for r in rule_nums]))
        # print("(?:" + "|".join(result) + ")")
        return "(?:" + "|".join(result) + ")"


meta_rule = check_rule(0)
counter = 0

for message in messages:
    # print(meta_rule, message, bool(re.fullmatch(meta_rule, message)))
    counter += bool(re.fullmatch(meta_rule, message))

print(counter)