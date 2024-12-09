with open("inp", "r") as inp:
    expanded_line = []
    is_free = False
    curr_id = 0
    how_many_blocks = 0

    for char in inp.read().strip():
        if is_free and int(char) != 0:
            expanded_line.extend([-1] * int(char))
        elif int(char) != 0:
            expanded_line.extend([curr_id] * int(char))
            curr_id += 1
            how_many_blocks += int(char)

        is_free = not is_free 

    i = len(expanded_line) - 1
    free_space_idx = expanded_line.index(-1) # assume there is some free space

    while free_space_idx != how_many_blocks:
        expanded_line[free_space_idx] = expanded_line[i]
        expanded_line[i] = -1
        free_space_idx = expanded_line.index(-1)
        i -= 1

    checksum = 0
    for i in range(how_many_blocks):
        checksum += i * expanded_line[i]

    print(checksum)
