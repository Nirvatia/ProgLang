s1, s2, s3 = input().split(), input().split(), input().split()

res = len(s1[0]) * int(s1[1]) + len(s2[0]) * int(s2[1]) + len(s3[0]) * int(s3[1])

print(res)