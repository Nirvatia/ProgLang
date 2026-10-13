n, m, k = map(int, input().split())

sweets_needed = n * m

if sweets_needed % k == 0:
    print(sweets_needed // k)
else:
    print(sweets_needed // k + 1)