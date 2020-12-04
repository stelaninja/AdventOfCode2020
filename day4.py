import re

X = [x for x in open("input4.in").read().split("\n\n")]
Y = [y.split() for y in X]


req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
opt_fiels = ["cid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def make_passports(passport_data):
    pass_list = []
    for passport in passport_data:
        pass_dict = {}

        for key_val in passport:
            key_val_list = key_val.split(":")
            pass_dict[key_val_list[0]] = key_val_list[1]

        pass_list.append(pass_dict)

    return pass_list


def all_valid_fields(passport_list, req_fields):
    num_valid = 0
    valid_passports = []
    for passport in passport_list:
        check = True

        for field in req_fields:
            if field not in passport:
                check = False

        if check == True:
            num_valid += 1
            valid_passports.append(passport)

    return valid_passports


def validate_fields(passport, eye_colors):
    check = True

    for field in passport:

        if field == "byr":
            try:
                x = int(passport[field])
                if x < 1920 or x > 2002:
                    check = False
            except:
                check = False

        elif field == "iyr":
            try:
                x = int(passport[field])
                if x < 2010 or x > 2020:
                    check = False
            except:
                check = False

        elif field == "eyr":
            try:
                x = int(passport[field])
                if x < 2020 or x > 2030:
                    check = False
            except:
                check = False

        elif field == "hgt":
            try:
                length = int(passport[field][:-2])
                unit = passport[field][-2:]

                if unit == "cm":
                    if length < 150 or length > 193:
                        check = False
                elif unit == "in":
                    if length < 59 or length > 76:
                        check = False
                else:
                    check = False
            except:
                check = False

        elif field == "hcl":
            try:
                if not re.match(r"^#[a-f0-9]{6}$", passport[field]):
                    check = False
            except:
                check = False

        elif field == "ecl":
            try:
                if passport[field] not in eye_colors:
                    check = False
            except:
                check = False

        elif field == "pid":
            try:
                if not re.match(r"^\d{9}$", passport[field]):
                    check = False
            except:
                check = False

    if check == True:
        return 1
    else:
        return 0


passport_list = make_passports(Y)
valid_passports = all_valid_fields(passport_list, req_fields)

num_valid = 0

for passport in valid_passports:
    num_valid += validate_fields(passport, eye_colors)

print(f"Num of passports: {len(passport_list)}")
print(f"Part 1: {len(valid_passports)}")
print(f"Part 2: {num_valid}")
