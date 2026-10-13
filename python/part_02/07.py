from math import ceil

s = input().split()

n = int(s[0])
t = float(s[1])

res = ceil(n * 60 / t)

print(res)