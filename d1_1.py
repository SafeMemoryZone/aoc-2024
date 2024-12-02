with open("inp", "r") as inp:
    left = []
    right = []
    for line in inp:
        arr = line.strip().split()
        left.append(int(arr[0]))
        right.append(int(arr[1]))

    left.sort()
    right.sort()

    total_dist = 0
    for idx, el in enumerate(left):
        total_dist += abs(el - right[idx])
    
    print(total_dist)
