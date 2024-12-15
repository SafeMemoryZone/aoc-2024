move_to_off = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)
}

def get_box_mass(curr_box_row_idx, curr_box_col_idx, move, grid, curr_mass):
    if grid[curr_box_row_idx][curr_box_col_idx] == "]":
        curr_box_col_idx -= 1

    # base case: not possible to move
    if grid[curr_box_row_idx][curr_box_col_idx] == "#":
        return False

    # base case: possible to move
    if grid[curr_box_row_idx][curr_box_col_idx] == ".":
        return True

    curr_mass.append((curr_box_row_idx, curr_box_col_idx, "["))
    curr_mass.append((curr_box_row_idx, curr_box_col_idx + 1, "]"))

    nexts = []

    if move == ">":
        nexts.append(get_box_mass(curr_box_row_idx, curr_box_col_idx + 2, move, grid, curr_mass))
    elif move == "<":
        nexts.append(get_box_mass(curr_box_row_idx, curr_box_col_idx - 1, move, grid, curr_mass))
    elif move == "^":
        nexts.append(get_box_mass(curr_box_row_idx - 1, curr_box_col_idx, move, grid, curr_mass))
        nexts.append(get_box_mass(curr_box_row_idx - 1, curr_box_col_idx + 1, move, grid, curr_mass))
    elif move == "v":
        nexts.append(get_box_mass(curr_box_row_idx + 1, curr_box_col_idx, move, grid, curr_mass))
        nexts.append(get_box_mass(curr_box_row_idx + 1, curr_box_col_idx + 1, move, grid, curr_mass))

    # all boxes in front have to me movable
    return all(nexts)


def move_box(box_row_idx, box_col_idx, row_off, col_off, grid, move):
    box_mass = []
    is_movable = get_box_mass(box_row_idx, box_col_idx, move, grid, box_mass)

    if not is_movable:
        return False

    if move == ">":
        box_mass.sort(key=lambda x: x[1], reverse=True)
    elif move == "<":
        box_mass.sort(key=lambda x: x[1])
    elif move == "^":
        box_mass.sort(key=lambda x: x[0])
    elif move == "v":
        box_mass.sort(key=lambda x: x[0], reverse=True)

    for box in box_mass:
        grid[box[0]][box[1]] = "."
        calculated_row_idx = box[0] + row_off
        calculated_col_idx = box[1] + col_off

        grid[calculated_row_idx][calculated_col_idx] = box[2]

    return True


def do_move(curr_row_idx, curr_col_idx, move, grid):
    row_off, col_off = move_to_off[move]

    if grid[curr_row_idx + row_off][curr_col_idx + col_off] == "#":
        return curr_row_idx, curr_col_idx

    if grid[curr_row_idx + row_off][curr_col_idx + col_off] == ".":
        return curr_row_idx + row_off, curr_col_idx + col_off

    if not move_box(curr_row_idx + row_off, curr_col_idx + col_off, row_off, col_off, grid, move):
        return curr_row_idx, curr_col_idx
    
    return curr_row_idx + row_off, curr_col_idx + col_off

with open("inp", "r") as inp:
    grid = []
    moves = []
    robot_pos = tuple()
    
    for row_idx, line in enumerate(inp):
        if "#" in line:
            processed_row = []
            for col_idx, c in enumerate(list(line.strip())):
                if c == ".":
                    processed_row.append(".")
                    processed_row.append(".")
                elif c == "O":
                    processed_row.append("[")
                    processed_row.append("]")
                elif c == "#":
                    processed_row.append("#")
                    processed_row.append("#")
                elif c == "@":
                    robot_pos = (row_idx, col_idx * 2)
                    processed_row.append(".")
                    processed_row.append(".")
            grid.append(processed_row)
        else:
            moves.extend(list(line.strip()))

    curr_row_idx = robot_pos[0]
    curr_col_idx = robot_pos[1]

    for move in moves:
        curr_row_idx, curr_col_idx = do_move(curr_row_idx, curr_col_idx, move, grid)
    
    gps_sum = 0

    for row_idx, line in enumerate(grid):
        for col_idx, c in enumerate(line):
            if c == "[":
                gps_sum += row_idx * 100 + col_idx
    print(gps_sum)
