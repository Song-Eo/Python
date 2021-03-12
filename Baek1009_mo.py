T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        c = 10
    elif a == 1 or a == 5 or a == 6:
        c = a
    elif a == 4 or a == 9:
        if b % 2 == 1:
            c = a
        else:
            c = (a*a) % 10
    else:
        if b % 4 == 1:
            c = a
        elif b % 4 == 2:
            c = (a*a) % 10
        elif b % 4 == 3:
            c = (a**3) % 10
        else:
            c = (a**4) % 10
    print(c)
