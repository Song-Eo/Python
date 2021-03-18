N = int(input())
F = int(input())
N = N - (N%100)

x = int(N / F)
if N % F == 0:
    last = N
else:
    last = (x + 1) * F
last = str(last)

print(last[-2], last[-1], sep='')
