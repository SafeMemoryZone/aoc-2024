offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_at(row_idx, col_idx, garden):
    if row_idx < 0 or row_idx >= len(garden) or col_idx < 0 or col_idx >= len(garden[0]):
        return None

    return garden[row_idx][col_idx]

def calculate_region_cost(curr_row_idx, curr_col_idx, garden):
    plant_ty = garden[curr_row_idx][curr_col_idx] 
    tbp_plants = [(curr_row_idx, curr_col_idx)]
    perimeters_count = 0

    curr_plant_idx = 0
    while curr_plant_idx < len(tbp_plants):
        for off in offsets:
            calculated_idx = (tbp_plants[curr_plant_idx][0] + off[0], tbp_plants[curr_plant_idx][1] + off[1])

            if calculated_idx in set(tbp_plants):
                continue

            value = get_at(calculated_idx[0], calculated_idx[1], garden)

            if value == plant_ty:
                tbp_plants.append(calculated_idx)
            else:
                perimeters_count += 1

        curr_plant_idx += 1

    return len(tbp_plants) * perimeters_count, set(tbp_plants)

with open("inp", "r") as inp:
    garden = []

    for line in inp:
        garden.append(list(line.strip()))

    total_cost = 0
    processed_plants = set()

    for row_idx, line in enumerate(garden):
        for col_idx, p in enumerate(line):
            if (row_idx, col_idx) in processed_plants:
                continue

            cost, encountered = calculate_region_cost(row_idx, col_idx, garden)
            total_cost += cost
            processed_plants = processed_plants.union(encountered)

    print(total_cost)
