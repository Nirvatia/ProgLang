def decimal_to_binary(a):
    q = a
    res = []

    while q > 0:
        r = q % 2
        res.append(r)
        q //= 2

    res.reverse()
    return res

n = int(input())
nums = list(map(int, input().split()))

res = []
for i in nums:
    x_binary = decimal_to_binary(i)
    y_binary = decimal_to_binary(len(x_binary))
    z = len(y_binary)

    for i in range(z - 1):
        res.append(0)

    res.extend(y_binary)
    res.extend(x_binary[1:])

print(f"{''.join(map(str, res))}")