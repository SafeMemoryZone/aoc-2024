with open("inp", "r") as inp:
    stones = [int(x) for x in inp.read().strip().split()]

    for i in range(25):
        idx = 0
        while idx < len(stones):

            if stones[idx] == 0:
                stones[idx] = 1
                idx += 1

            elif len(str(stones[idx])) % 2 == 0:
                length = len(str(stones[idx]))
                first = int(str(stones[idx])[:length // 2])
                second = int(str(stones[idx])[length // 2:])

                stones.insert(idx, first)
                stones.insert(idx + 1, second)
                stones.pop(idx + 2)
                idx += 2

            else:
                stones[idx] *= 2024
                idx += 1

        print(f"{i} of 24")


    print(len(stones))
