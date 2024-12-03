def is_safe(report):
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

    return not is_unsafe

with open("inp", "r") as inp:
    safe_count = 0

    for line in inp:
        report = [int(x) for x in line.strip().split()]

        for i in range(len(report)):
            modified_report = report.copy()
            modified_report.pop(i)
            if is_safe(modified_report):
                safe_count += 1
                break

    print(safe_count)
