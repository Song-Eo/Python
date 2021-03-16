a, b, c = map(int, input().split())
total = 0

if b >= c:
    print(-1)

else:
    x = a / (c-b)
    print(int(x)+1)




