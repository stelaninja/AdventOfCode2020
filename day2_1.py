X = [x for x in open("input2.in").read().splitlines()]


def part_one():
    num_valid_pwds = 0
    for pw in X:
        pw_list = pw.split()
        nums = pw_list[0].split("-")
        low = int(nums[0])
        hi = int(nums[1])
        char = pw_list[1][:1]
        pwd = pw_list[2]
        num_occ = pwd.count(char)

        if num_occ >= low and num_occ <= hi:
            num_valid_pwds += 1

    return num_valid_pwds


def part_two():
    num_valid_pwds = 0
    for pw in X:
        pw_list = pw.split()
        nums = pw_list[0].split("-")
        low = int(nums[0])
        hi = int(nums[1])
        char = pw_list[1][:1]
        pwd = pw_list[2]

        if (pwd[low - 1] == char or pwd[hi - 1] == char) and pwd[low - 1] != pwd[
            hi - 1
        ]:
            num_valid_pwds += 1
            print(low, hi, pwd[low - 1], pwd[hi - 1], pwd)

    return num_valid_pwds


print(part_one())
print(part_two())

