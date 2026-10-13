n = int(input())

masha_score = 0
dasha_score = 0

while n > 0:
    num = int(input())

    if num % 3 == 0:
        masha_score += 2
    else:
        dasha_score += 1
    n -= 1

print(f"{masha_score}:{dasha_score}")