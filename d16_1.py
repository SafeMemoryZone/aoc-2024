import heapq

offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_cost(grid):
    distances = []
    end_pos = tuple()

    for row_idx, line in enumerate(grid):
        for col_idx, c in enumerate(line):
            if c == "S":
                heapq.heappush(distances, (0, row_idx, col_idx, (0, 1)))
            elif c == "E":
                end_pos = (row_idx, col_idx)

    visited = set()

    while len(distances) != 0:
        dist, curr_row_idx, curr_col_idx, curr_dir = heapq.heappop(distances)

        if (curr_row_idx, curr_col_idx, curr_dir) in visited:
            continue

        visited.add((curr_row_idx, curr_col_idx, curr_dir))

        if curr_row_idx == end_pos[0] and curr_col_idx == end_pos[1]:
            return dist
        
        for off in offsets:
            next_row_idx = curr_row_idx + off[0]
            next_col_idx = curr_col_idx + off[1]

            if grid[next_row_idx][next_col_idx] == "#":
                continue

            cost = dist + 1 if off == curr_dir else dist + 1001

            heapq.heappush(distances, (cost, next_row_idx, next_col_idx, off))

    return -1 # no path

with open("inp", "r") as inp:
    grid = [list(x.strip()) for x in inp.read().split("\n")]

    print(find_cost(grid))
