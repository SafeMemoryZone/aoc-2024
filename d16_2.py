import heapq
import copy

offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find_tiles_on_best_paths(grid):
    distances = []
    end_pos = tuple()
    start_pos = tuple()

    for row_idx, line in enumerate(grid):
        for col_idx, c in enumerate(line):
            if c == "S":
                heapq.heappush(distances, (0, row_idx, col_idx, 2))
                start_pos = (row_idx, col_idx)
            elif c == "E":
                end_pos = (row_idx, col_idx)

    visited = set()
    best_ways = {(start_pos[0], start_pos[1], 2): (0, {start_pos})}

    while len(distances) != 0:
        dist, curr_row_idx, curr_col_idx, curr_dir = heapq.heappop(distances)

        if (curr_row_idx, curr_col_idx, curr_dir) in visited:
            continue

        visited.add((curr_row_idx, curr_col_idx, curr_dir))

        for new_dir, off in enumerate(offsets):
            next_row_idx = curr_row_idx + off[0]
            next_col_idx = curr_col_idx + off[1]

            if (
                next_row_idx < 0
                or next_row_idx >= len(grid)
                or next_col_idx < 0
                or next_col_idx >= len(grid[0])
            ):
                continue
            if grid[next_row_idx][next_col_idx] == "#":
                continue

            cost = dist + 1 if new_dir == curr_dir else dist + 1000
            curr_path = copy.deepcopy(
                best_ways[(curr_row_idx, curr_col_idx, curr_dir)][1]
            )
            curr_path.add((next_row_idx, next_col_idx))

            if (next_row_idx, next_col_idx, new_dir) not in best_ways:
                best_ways[(next_row_idx, next_col_idx, new_dir)] = (cost, curr_path)
            else:
                best_score = best_ways[(next_row_idx, next_col_idx, new_dir)][0]
                if cost < best_score:
                    best_ways[(next_row_idx, next_col_idx, new_dir)] = (cost, curr_path)
                elif cost == best_score:
                    best_ways[(next_row_idx, next_col_idx, new_dir)] = (
                        best_score,
                        best_ways[(next_row_idx, next_col_idx, new_dir)][1].union(
                            curr_path
                        ),
                    )

            heapq.heappush(distances, (cost, next_row_idx, next_col_idx, new_dir))

    min_cost = float("inf")
    best_paths = set()

    for d in range(4):
        if (end_pos[0], end_pos[1], d) in best_ways:
            cost, path = best_ways[(end_pos[0], end_pos[1], d)]
            if cost < min_cost:
                min_cost = cost
                best_paths = path
            elif cost == min_cost:
                best_paths = best_paths.union(path)

    return len(best_paths)


with open("inp", "r") as inp:
    grid = [list(x.strip()) for x in inp.read().split("\n")]
    print(find_tiles_on_best_paths(grid))
