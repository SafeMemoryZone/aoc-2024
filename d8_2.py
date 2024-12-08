import math

with open("inp", "r") as inp:
    antennas = {}
    grid = []

    for row_idx, line in enumerate(inp):
        for col_idx, c in enumerate(line.strip()):
            if c == ".":
                continue
            elif c in antennas:
                antennas[c].append((row_idx, col_idx))
            else:
                antennas[c] = [(row_idx, col_idx)]

        grid.append(list(line.strip()))

    antinode_poses = set()
    grid_row_count = len(grid)
    grid_col_count = len(grid[0])

    for antenna_freq in antennas.keys():
        curr_poses = antennas[antenna_freq]

        for curr_idx, start_pos in enumerate(curr_poses):
            for end_pos in curr_poses:
                if end_pos == start_pos:
                    continue

                shift = (start_pos[0] - end_pos[0], start_pos[1] - end_pos[1])

                # simplify 
                denom = math.gcd(shift[0], shift[1])
                shift = (shift[0] // denom, shift[1] // denom)
                
                curr_pos = (end_pos[0], end_pos[1])

                while curr_pos[0] >= 0 and curr_pos[0] < grid_row_count and curr_pos[1] >= 0 and curr_pos[1] < grid_col_count:
                    antinode_poses.add(curr_pos)
                    curr_pos = (curr_pos[0] + shift[0], curr_pos[1] + shift[1])

    print(len(antinode_poses))
