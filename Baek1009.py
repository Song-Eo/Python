T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    s, c = 0, 1
    for s in range(b):
        c *= a
    print(c % 10)

