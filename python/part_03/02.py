t = int(input())

while t > 0:
    n = int(input())
    p, q = map(int, input().split())

    res = []
    curr = p

    while n > 0:
        curr *= 2

        if curr >= q:
            res.append(1)
            curr -= q
        else:
            res.append(0)
        n -= 1

    print(f"0.{''.join(map(str, res))}")

    t -= 1

