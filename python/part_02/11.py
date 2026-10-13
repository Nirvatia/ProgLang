s = input().split()

for i in range(len(s)):
    print(f'{"".join(reversed(s[i]))}{"" if i == len(s) - 1 else " "}', end="")