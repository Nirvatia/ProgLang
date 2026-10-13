from math import floor, ceil

x, y = map(float, input().split())

res = floor(y) - ceil(x) + 1

print(res)