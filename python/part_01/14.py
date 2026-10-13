n, a = map(int, input().split())

cnt = 0
curr = a

while cnt < n:
    if curr % 2 != 0 and curr % 3 != 0 and curr % 5 != 0 and curr % 7 != 0:
        print(curr)
        cnt += 1
    curr += 1
