move_to_off = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0)
}

def do_move(curr_row_idx, curr_col_idx, move, grid):
    row_off, col_off = move_to_off[move]
    front = grid[curr_row_idx + row_off][curr_col_idx + col_off] 

    if front == ".":
        return curr_row_idx + row_off, curr_col_idx + col_off

    if front == "#":
        return curr_row_idx, curr_col_idx

    # find free space
    free_row_idx = curr_row_idx + 2 * row_off
    free_col_idx = curr_col_idx + 2 * col_off
    found = False

    while grid[free_row_idx][free_col_idx] != "#":
        if grid[free_row_idx][free_col_idx] == ".":
            found = True
            break
        free_row_idx += row_off
        free_col_idx += col_off

    if not found:
        return curr_row_idx, curr_col_idx

    grid[curr_row_idx + row_off][curr_col_idx + col_off] = "."
    grid[free_row_idx][free_col_idx] = "O"

    return curr_row_idx + row_off, curr_col_idx + col_off

with open("inp", "r") as inp:
    grid = []
    moves = []
    robot_pos = tuple()
    
    for row_idx, line in enumerate(inp):
        if "#" in line:
            row = list(line.strip())
            if "@" in row:
                robot_pos = (row_idx, row.index("@"))
                row[robot_pos[1]] = "." # to avoid later problems
            grid.append(row)
        else:
            moves.extend(list(line.strip()))

    curr_row_idx = robot_pos[0]
    curr_col_idx = robot_pos[1]

    for move in moves:
        curr_row_idx, curr_col_idx = do_move(curr_row_idx, curr_col_idx, move, grid)
    
    gps_sum = 0
    for row_idx, row in enumerate(grid):
        for col_idx, c in enumerate(row):
            if c == "O":
                gps_sum += row_idx * 100 + col_idx

    print(gps_sum)
