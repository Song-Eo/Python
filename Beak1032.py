N = int(input())
for i in range(N):
    b = input()
    if i == 0:
        a = b
        a = list(a)
    else:
        for j in range(len(a)):
            if a[j] != b[j]:
                a[j] = '?'

for i in range(len(a)):
    print(a[i], end='')