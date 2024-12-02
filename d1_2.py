with open("inp", "r") as inp:
    left = []
    right = []
    for line in inp:
        arr = line.strip().split()
        left.append(int(arr[0]))
        right.append(int(arr[1]))

    sim_score = 0
    for idx, el in enumerate(left):
        sim_score += el * right.count(el)
    
    print(sim_score)
