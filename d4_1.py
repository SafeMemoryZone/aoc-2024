possible_offsets = [
    # horizontal
    [(0, 0, "X"), (0, 1, "M"), (0, 2, "A"), (0, 3, "S")],
    [(0, 0, "X"), (0, -1, "M"), (0, -2, "A"), (0, -3, "S")],
    # vertical
    [(0, 0, "X"), (1, 0, "M"), (2, 0, "A"), (3, 0, "S")],
    [(0, 0, "X"), (-1, 0, "M"), (-2, 0, "A"), (-3, 0, "S")],
    # diagonal (right-up)
    [(0, 0, "X"), (-1, 1, "M"), (-2, 2, "A"), (-3, 3, "S")],
    # diagonal (right-down)
    [(0, 0, "X"), (1, 1, "M"), (2, 2, "A"), (3, 3, "S")],
    # diagonal (left-up)
    [(0, 0, "X"), (-1, -1, "M"), (-2, -2, "A"), (-3, -3, "S")],
    # diagonal (left-down)
    [(0, 0, "X"), (1, -1, "M"), (2, -2, "A"), (3, -3, "S")],
]


def get_at(row_idx, col_idx, arr):
    if row_idx < 0 or row_idx >= len(arr) or col_idx < 0 or col_idx >= len(arr[0]):
        return None
    return arr[row_idx][col_idx]


with open("inp", "r") as inp:
    lines = inp.read().strip().split("\n")
    count = 0

    for row_idx in range(len(lines)):
        for col_idx in range(len(lines)):
            for possible_off in possible_offsets:
                found_xmas = True

                for row_off, col_off, req_char in possible_off:
                    if get_at(row_idx + row_off, col_idx + col_off, lines) != req_char:
                        found_xmas = False
                        break

                if found_xmas:
                    count += 1

    print(count)
