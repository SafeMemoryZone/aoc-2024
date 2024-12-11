def insert_or_update(di, key, value):
    if key in di:
        di[key] += value
    else:
        di[key] = value

with open("inp", "r") as inp:
    curr_state = {}

    for x in inp.read().strip().split():
        if int(x) in curr_state:
            curr_state[int(x)] += 1
        else:
            curr_state[int(x)] = 1

    for _ in range(25):
        next_state = {}

        for key, value in curr_state.items():
            if key == 0:
                insert_or_update(next_state, 1, value)

            elif len(str(key)) % 2 == 0:
                mid = len(str(key)) // 2
                left = int(str(key)[:mid])
                right = int(str(key)[mid:])

                insert_or_update(next_state, left, value)
                insert_or_update(next_state, right, value)
            else:
                insert_or_update(next_state, key * 2024, value)

        curr_state = next_state

    count = 0
    for val in curr_state.values():
        count += val

    print(count)
