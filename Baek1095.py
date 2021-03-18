<<<<<<< HEAD
S, F, M = map(int, input().split())
glass = S + F
Com = 1
last = -1

if S != 1:
    for i in range(1, S+1):
        Com *= i
    Com = int((glass * S) / Com)

    for i in range(M, 1, -1):
        if Com % i == 0:
            last = i
            break

else:
    if glass <= M:
        last = glass

=======
S, F, M = map(int, input().split())
glass = S + F
Com = 1
last = -1

if S != 1:
    for i in range(1, S+1):
        Com *= i
    Com = int((glass * S) / Com)

    for i in range(M, 1, -1):
        if Com % i == 0:
            last = i
            break

else:
    if glass <= M:
        last = glass

>>>>>>> 7eb5bd33e4f2e112f3f4283c39e449a2ab383a47
print(last)