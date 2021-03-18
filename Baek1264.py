S = []
c = []
while True:
    Sen = input()
    S.append(Sen)
    if Sen == '#':
        break

for i in range(len(S)-1):
    c.append(0)
    for j in S[i].lower():
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            c[i] += 1

for i in range(len(S)-1):
    print(c[i])