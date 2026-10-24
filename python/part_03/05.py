def binary_to_decimal(n):
    res = 0

    for i in range(len(n)):
        res += int(n[i]) * 2 ** (len(n) - i - 1)

    return res

seq = input()

res = []
total_nums = 0
while len(seq) > 0:
    z = 0
    for i in seq:
        if i == '0':
            z += 1
        else:
            seq = seq[z:]
            break

    y_binary = seq[:z + 1]
    y_decimal = binary_to_decimal(y_binary)
    seq = seq[z + 1:]

    x_binary = '1' + seq[:y_decimal - 1]
    x_decimal = binary_to_decimal(x_binary)
    seq = seq[y_decimal - 1:]

    total_nums += 1
    res.append(x_decimal)

print(f"{total_nums}")
for n in res:
    print(f"{n} ", end="")


