def is_correct_order(update, rules):
    encountered = set()
    update_set = set(update)

    for num in update:
        if num not in rules:
            encountered.add(num)
            continue
        else:
            for pred in rules[num]:
                if pred not in encountered and pred in update_set:
                    return False
        encountered.add(num)

    return True


with open("inp", "r") as inp:
    updates = []
    rules = {}
    for line in inp:
        if line.strip() == "":
            continue
        if "|" not in line :
            updates.append([int(x) for x in line.strip().split(",")])
        else:
            arr = [int(x) for x in line.strip().split("|")]
            if arr[1] in rules:
                rules[arr[1]].append(arr[0])
            else:
                rules[arr[1]] = [arr[0]]

    score = 0
    for update in updates:
        if is_correct_order(update, rules):
            score += update[len(update) // 2]

    print(score)
