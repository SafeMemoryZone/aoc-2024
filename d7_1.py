def get_next_comb(arr, curr_idx=0):
    if curr_idx >= len(arr):
        return

    if arr[curr_idx]:
        arr[curr_idx] = False
        get_next_comb(arr, curr_idx + 1)
    else:
        arr[curr_idx] = True

def is_possible(target, values):
    op_count = (len(values) - 1)
    is_plus_ops = [False] * op_count

    for _ in range(2 ** op_count):
        curr_val = values[0]

        for curr_idx, is_plus_op in enumerate(is_plus_ops):
            if is_plus_op:
                curr_val += values[curr_idx + 1]
            else:
                curr_val *= values[curr_idx + 1]

        if curr_val == target:
            return True

        get_next_comb(is_plus_ops)

    return False

with open("inp", "r") as inp:
    curr_sum = 0

    for line in inp:
        colon_idx = line.index(":")
        target, values = int(line[:colon_idx]), [int(x) for x in line[colon_idx + 1:].strip().split()]

        if is_possible(target, values):
            curr_sum += target

    print(curr_sum)
