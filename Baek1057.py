n, k, l = map(int, input().split())
r = 0
while True:

    if k - l == 1 or l - k == 1:
        if (int(k/2)+1 == l/2) or (int(l/2)+1 == k/2):
            r += 1
            break
        else:
            k = int(k / 2 + 0.5)
            l = int(l / 2 + 0.5)
    else:
        k = int(k/2+0.5)
        l = int(l/2+0.5)

    r += 1

print(r)
