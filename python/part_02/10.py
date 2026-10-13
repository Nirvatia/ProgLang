s = input()

res = ''

for c in reversed(s):
    if c == '(':
        res += ')'
    else:
        res += '('

print(res)