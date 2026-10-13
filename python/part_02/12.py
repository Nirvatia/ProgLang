def find_lowest_divisor(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2

    return n

nums = map(int, input().split())

for num in nums:
    print(f"{find_lowest_divisor(num)} ", end="")
