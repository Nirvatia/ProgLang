n = int(input())

curr = n

print(curr)

while curr > 1:
    if curr % 2 == 0:
        curr //= 2
    else:
        curr = 3 * curr + 1
    print(curr)
