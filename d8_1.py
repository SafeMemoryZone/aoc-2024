with open("inp", "r") as inp:
    antennas = {}
    grid_row_count = 0
    grid_col_count = 0

    for row_idx, line in enumerate(inp):
        for col_idx, c in enumerate(line.strip()):
            if c == ".":
                grid_col_count = col_idx + 1
                continue
            elif c in antennas:
                antennas[c].append((row_idx, col_idx))
            else:
                antennas[c] = [(row_idx, col_idx)]

            grid_col_count = col_idx + 1

        grid_row_count = row_idx + 1

    antinode_poses = set()

    for antenna_freq in antennas.keys():
        curr_poses = antennas[antenna_freq]

        for curr_idx, start_pos in enumerate(curr_poses):
            for end_pos in curr_poses:
                if end_pos == start_pos:
                    continue
                antinode_pos = (2 * start_pos[0] - end_pos[0], 2 * start_pos[1] - end_pos[1])
                if antinode_pos[0] < 0 or antinode_pos[1] < 0 or antinode_pos[0] >= grid_row_count or antinode_pos[1] >= grid_col_count:
                    continue

                antinode_poses.add(antinode_pos)            

    print(len(antinode_poses))
