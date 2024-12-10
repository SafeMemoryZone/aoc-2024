offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_at(grid, row_idx, col_idx):
    if row_idx < 0 or row_idx >= len(grid) or col_idx < 0 or col_idx >= len(grid[0]):
        return None
    return grid[row_idx][col_idx]

def get_rating(grid, start_row_idx, start_col_idx, curr_num, curr_trail, trails):
    curr_trail.append((start_row_idx, start_col_idx))

    if grid[start_row_idx][start_col_idx] == 9:
        trails.append(curr_trail[:])
        curr_trail.pop()
        return

    target_num = curr_num + 1

    for off in offsets:
        if get_at(grid, start_row_idx + off[0], start_col_idx + off[1]) == target_num:
            get_rating(grid, start_row_idx + off[0], start_col_idx + off[1], target_num, curr_trail, trails)

    curr_trail.pop()

def count_unique(trails):
    encountered = set()
    for trail in trails:
        encountered.add(tuple(trail))

    return len(encountered)

with open("inp", "r") as inp:
    grid = []
    for line in inp:
        grid.append([int(x) for x in line.strip()])

    score = 0
    for row_idx, line in enumerate(grid):
        for col_idx, c in enumerate(line):
            if c == 0:
                trails = []
                get_rating(grid, row_idx, col_idx, 0, [], trails)
                score += count_unique(trails)

    print(score)
