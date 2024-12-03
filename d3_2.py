import re

with open("inp", "r") as inp:
    insts = inp.read().strip()
    muls = re.findall(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)", insts)
    curr_sum = 0

    enabled = True

    for mul in muls:
        if mul == "do()":
            enabled = True
        elif mul == "don't()":
            enabled = False
        elif enabled:
            first = int(mul[4:mul.index(",")])
            second = int(mul[mul.index(",") + 1:-1])
            curr_sum += first * second

    print(curr_sum)
