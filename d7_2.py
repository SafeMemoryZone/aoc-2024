def get_next_comb(arr, curr_idx=0):
    if curr_idx >= len(arr):
        return

    if arr[curr_idx] == "+":
        arr[curr_idx] = "*"
    elif arr[curr_idx] == "*":
        arr[curr_idx] = "||"
    elif arr[curr_idx] == "||":
        arr[curr_idx] = "+"
        get_next_comb(arr, curr_idx + 1)

def is_possible(target, values):
    op_count = (len(values) - 1)
    ops = ["+"] * op_count

    for _ in range(3 ** op_count):
        curr_val = values[0]

        for curr_idx, op in enumerate(ops):
            if op == "+":
                curr_val += values[curr_idx + 1]
            elif op == "*":
                curr_val *= values[curr_idx + 1]
            elif op == "||":
                curr_val = int(str(curr_val) + str(values[curr_idx + 1]))

        if curr_val == target:
            return True

        get_next_comb(ops)

    return False

with open("inp", "r") as inp:
    curr_sum = 0

    for idx, line in enumerate(inp):
        colon_idx = line.index(":")
        target, values = int(line[:colon_idx]), [int(x) for x in line[colon_idx + 1:].strip().split()]

        if is_possible(target, values):
            curr_sum += target

        print(f"{idx} out of 849 done")

    print(curr_sum)
