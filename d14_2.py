with open("inp", "r") as inp:
    robots = []

    for line in inp:
        parsed = line.strip().split()
        init_pos = [int(x) for x in parsed[0][parsed[0].index("=") + 1:].split(",")]
        velocity = [int(x) for x in parsed[1][parsed[1].index("=") + 1:].split(",")]

        robots.append([init_pos, velocity])

    min_sf = float("inf")
    best_iter = None

    for i in range(101 * 103):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0

        for robot in robots:
            init_pos_x = robot[0][0]
            init_pos_y = robot[0][1]

            vel_x = robot[1][0]
            vel_y = robot[1][1]

            pos_x = (init_pos_x + vel_x * i) % 101
            pos_y = (init_pos_y + vel_y * i) % 103

            if pos_x > 50 and pos_y > 51:
                q1 += 1
            elif pos_x < 50 and pos_y > 51:
                q2 += 1
            elif pos_x < 50 and pos_y < 51:
                q3 += 1
            elif pos_x > 50 and pos_y < 51:
                q4 += 1

        curr_sf = q1 * q2 * q3 * q4

        if curr_sf < min_sf:
            min_sf = curr_sf
            best_iter = i

    print(min_sf, best_iter)
