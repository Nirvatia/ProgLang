w1, w2, w3 = input().split()

l1 = len(w1)
l2 = len(w2)
l3 = len(w3)

if l1 > l2 and l1 > l3:
    print(w1)
elif l2 > l1 and l2 > l3:
    print(w2)
else:
    print(w3)