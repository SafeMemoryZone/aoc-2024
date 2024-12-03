with open("inp", "r") as inp:
    safe_count = 0

    for line in inp:
        report = [int(x) for x in line.strip().split()]

        is_increasing = report[1] > report[0]
        prev_num = report[0]
        is_unsafe = False

        for num in report[1:]:
            if (num > prev_num) != is_increasing:
                is_unsafe = True
                break

            diff = abs(prev_num - num)

            if diff < 1 or diff > 3:
                is_unsafe = True
                break

            prev_num = num

        if not is_unsafe:
            safe_count += 1
    
    print(safe_count)
