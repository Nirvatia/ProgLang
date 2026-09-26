a, b, c = map(int, input().split())

if c >= min(a, b) and c <= max(a, b):
    print(0)
else:
    print(min(abs(a - c), abs(b - c)))