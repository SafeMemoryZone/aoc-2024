def copy_and_clean(arr, dst_idx, src_idx, clen):
    if src_idx <= dst_idx:
        exit(1)
    for i in range(clen):
       arr[dst_idx + i] = arr[src_idx + i] 
       arr[src_idx + i] = -1

with open("inp", "r") as inp:
    expanded_line = []
    is_free = False
    free_spaces = []
    files = []
    curr_idx = 0
    curr_id = 0

    for char in inp.read().strip():
        if is_free and int(char) != 0:
            expanded_line.extend([-1] * int(char))
            free_spaces.append((int(char), curr_idx))
        elif int(char) != 0:
            expanded_line.extend([curr_id] * int(char))
            files.append((int(char), curr_idx))
            curr_id += 1

        is_free = not is_free 
        curr_idx += int(char)

    for file_idx in range(len(files) - 1, -1, -1):
        free_idx = 0
        while free_idx < len(free_spaces):
            if free_spaces[free_idx][0] >= files[file_idx][0] and free_spaces[free_idx][1] < files[file_idx][1]:
                copy_and_clean(expanded_line, free_spaces[free_idx][1], files[file_idx][1], files[file_idx][0])
                if free_spaces[free_idx][0] - files[file_idx][0] <= 0:
                    free_spaces.pop(free_idx)
                else:
                    free_spaces[free_idx] = (free_spaces[free_idx][0] - files[file_idx][0], free_spaces[free_idx][1] + files[file_idx][0])
                break
            free_idx += 1

    checksum = 0

    for idx, c in enumerate(expanded_line):
        if c != -1:
           checksum += idx * c 

    print(checksum)
