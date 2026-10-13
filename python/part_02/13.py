n = int(input())

sum_divisors = 1

i = 2
while i <= n // 2:
    if n % i == 0:
        sum_divisors += i

    i += 1

print(sum_divisors)