def get_combs(button_a_x, button_a_y, button_b_x, button_b_y, target_x, target_y):
    button_a_clicks = 0
    button_b_clicks = 0

    cheapest_price = float("inf")

    while ((button_a_clicks * button_a_x) < target_x) and ((button_a_clicks * button_a_y) < target_y):
        curr_x = button_a_clicks * button_a_x
        curr_y = button_a_clicks * button_a_y

        while ((curr_x + button_b_clicks * button_b_x) < target_x) and ((curr_y + button_b_clicks * button_b_y) < target_y):
            button_b_clicks += 1

        curr_x = button_a_clicks * button_a_x + button_b_clicks * button_b_x
        curr_y = button_a_clicks * button_a_y + button_b_clicks * button_b_y

        if (curr_x == target_x) and (curr_y == target_y) and ((button_b_clicks + button_a_clicks * 3) < cheapest_price):
            cheapest_price = button_b_clicks + button_a_clicks * 3
        
        button_b_clicks = 0
        button_a_clicks += 1

    curr_x = button_a_clicks * button_a_x + button_b_clicks * button_b_x
    curr_y = button_a_clicks * button_a_y + button_b_clicks * button_b_y

    if (curr_x == target_x) and (curr_y == target_y) and ((button_b_clicks + button_a_clicks * 3) < cheapest_price):
        cheapest_price = button_b_clicks + button_a_clicks * 3

    return cheapest_price if cheapest_price != float("inf") else 0

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

        target_x = game[2][0]
        target_y = game[2][1] 


        total_price += get_combs(button_a_x, button_a_y, button_b_x, button_b_y, target_x, target_y)

    print(total_price)
