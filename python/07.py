a, b, c = map(int, input().split())

if a == b and b == c:
    print("hole")
else:
    print(a + b + c)