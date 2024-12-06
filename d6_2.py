# This solution is insanely inefficient, but it's simple

def get_at(row_idx, col_idx, pmap):
    if row_idx < 0 or row_idx >= len(pmap) or col_idx < 0 or col_idx >= len(pmap[0]):
        return None

    return pmap[row_idx][col_idx]

guard_face_map = {
        0: (-1, 0), # up
        1: (0, 1), # right
        2: (1, 0), # down
        3: (0, -1), # left
}

def step(guard_face, guard_pos, pmap):
    # returns: new_face, new_pos, continue
    off = guard_face_map[guard_face]
    char = get_at(guard_pos[0] + off[0], guard_pos[1] + off[1], pmap)

    if char is None:
        return guard_face, guard_pos, False

    if char == "#":
        return (guard_face + 1) % 4, guard_pos, True

    return guard_face, (guard_pos[0] + off[0], guard_pos[1] + off[1]), True


with open("inp", "r") as inp:
    pmap = []
    guard_pos = tuple()

    i = 0
    for line in inp:
        pmap.append(list(line.strip()))
        pos = line.strip().find("^")  # Note: We assume that the guard is always facing up

        if pos != -1:
            guard_pos = (i, pos)

        i += 1

    combs = 0

    for row_idx in range(len(pmap)):
        for col_idx in range(len(pmap[0])):
            print(f"{row_idx * len(pmap) + col_idx} out of {(len(pmap) - 1) * len(pmap) + len(pmap[0])}")
            if (row_idx, col_idx) == guard_pos:
                continue

            if pmap[row_idx][col_idx] != ".":
                continue

            pmap[row_idx][col_idx] = "#"

            curr_face = 0
            curr_pos = guard_pos
            should_continue = True
            unique_state = {(curr_face, curr_pos)}

            while should_continue:
                curr_face, curr_pos, should_continue = step(curr_face, curr_pos, pmap) 

                if (curr_face, curr_pos) in unique_state and should_continue:
                    combs += 1
                    break

                unique_state.add((curr_face, curr_pos))

            pmap[row_idx][col_idx] = "."

    print(combs)
