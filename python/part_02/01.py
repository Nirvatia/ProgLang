n = int(input())

MAX_PER_BUS = 15

q = n // MAX_PER_BUS
r = n % MAX_PER_BUS

print(f"{MAX_PER_BUS * q} {r}")