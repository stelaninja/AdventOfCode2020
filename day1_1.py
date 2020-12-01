values = [int(line.rstrip("\n")) for line in open("input1.txt", "r")]


def find_pairs_adding_to_target(target, values):
    values_sorted = sorted(values)
    low = 0
    hi = len(values) - 1

    while low < hi:
        sum_of_pairs = values_sorted[low] + values_sorted[hi]
        if sum_of_pairs < target:
            low += 1
        elif sum_of_pairs > target:
            hi -= 1
        else:
            return values_sorted[low], values_sorted[hi]

    raise ValueError(f"No pairs adds up to {target}.")


def find_triplets_adding_to_target(target, values):
    values_sorted = sorted(values)
    low = 0
    hi = len(values) - 1

    while low < hi:
        for i in range(low + 1, hi):
            sum_of_triplet = values_sorted[low] + values_sorted[i] + values_sorted[hi]
            if sum_of_triplet == target:
                return values_sorted[low], values_sorted[i], values_sorted[hi]
        if sum_of_triplet < target:
            low += 1
        elif sum_of_triplet > target:
            hi -= 1
        else:
            return values_sorted[low], values_sorted[i], values_sorted[hi]

    raise ValueError(f"No triplets adds up to {target}.")


x, y = find_pairs_adding_to_target(2020, values)
print(x * y)

x, y, z = find_triplets_adding_to_target(2020, values)
print(x * y * z)
