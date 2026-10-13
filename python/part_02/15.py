n = int(input())

res = 0

while n > 0:
    p, c = map(int, input().split())

    if p - c > 0:
        res += (p - c)
        
    n -= 1

print(res)