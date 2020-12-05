X = [x for x in open("input5.in").read().splitlines()]

# Test data
# X = ["FBFBBFFRLR"]


def find_seat(seat_data):
    # print(seat_data)
    max_row = 127
    min_row = 0
    max_col = 7
    min_col = 0
    row = seat_data[:7]
    col = seat_data[7:]

    # print(row, col)

    for r in row:
        if r == "F":
            max_row = (max_row + min_row) // 2
            # print(r, min_row, max_row)
        elif r == "B":
            min_row = (max_row + min_row) // 2 + 1
            # print(r, min_row, max_row)

        if min_row == max_row:
            row_num = min_row

    for c in col:
        if c == "L":
            max_col = (max_col + min_col) // 2
            # print(c, min_col, max_col)
        elif c == "R":
            min_col = (max_col + min_col) // 2 + 1
            # print(c, min_col, max_col)
        if min_col == max_col:
            col_num = min_col

    return row_num * 8 + col_num


seat_list = []
for seat_data in X:
    seat_list.append(find_seat(seat_data))

seat_list.sort()
# print(seat_list)

# print(row, col)
for i in range(1, len(seat_list) - 1):
    if seat_list[i - 1] != seat_list[i] - 1:
        print(seat_list[i] - 1)

# INCORRECT PART 2: 718 (forgot to choose the seat in front of 718)
