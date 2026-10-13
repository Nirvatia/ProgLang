h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

startInSeconds = h1 * 3600 + m1 * 60 + s1
endInSeconds = h2 * 3600 + m2 * 60 + s2

res = endInSeconds - startInSeconds

print(res)