def calculate_price(button_a_x, button_a_y, button_b_x, button_b_y, target_x, target_y):
    a_press = (target_x * button_b_y - target_y * button_b_x) / (button_a_x * button_b_y - button_a_y * button_b_x)
    b_press = (button_a_y * target_x - button_a_x * target_y) / (button_a_y * button_b_x - button_a_x * button_b_y)

    if int(a_press) != a_press or int(b_press) != b_press:
        return 0

    return int(a_press) * 3 + int(b_press)

with open("inp", "r") as inp:
    games = [[]]
    curr_game_idx = 0

    for line in inp:
        if line.strip() == "":
            games.append([])
            curr_game_idx += 1
            continue
        
        sep_idx = -1

        if "Button" in line:
            sep_idx = line.find("+")
        else:
            sep_idx = line.find("=")

        comma_idx = line.find(",")
        x_shift = int(line[sep_idx + 1: comma_idx])
        y_shift = int(line[comma_idx + 4:])
        games[curr_game_idx].append((x_shift, y_shift))

    total_price = 0

    for game in games:
        # costs 3
        button_a_x = game[0][0]
        button_a_y = game[0][1]

        # costs 1
        button_b_x = game[1][0]
        button_b_y = game[1][1]

        target_x = game[2][0] + 10000000000000
        target_y = game[2][1] + 10000000000000


        total_price += calculate_price(button_a_x, button_a_y, button_b_x, button_b_y, target_x, target_y)

    print(total_price)
