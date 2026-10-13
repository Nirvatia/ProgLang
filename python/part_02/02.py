s = input()

length = len(s)
mid = length // 2

start = s[0:mid]
end = s[mid:]

print(int(start) + int(end))

