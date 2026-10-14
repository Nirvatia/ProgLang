t = int(input())

while t > 0:
    p1, q1, p2, q2, p3, q3, p4, q4 = map(int, input().split())

    e = q1 * q2
    a = p1 * q2
    b = p2 * q1

    f = q3 * q4
    c = p3 * q4
    d = p4 * q3

    x = a + b
    y = c + d

    z = e * f
    x *= f
    y *= e

    if x > y:
        print('1 ', end='')
    elif x < y:
        print('-1 ', end='')
    else:
        print('0 ', end='')

    t -= 1


