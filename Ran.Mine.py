import random as r

col, row, mine = map(int, input().split())
dk = [-1, 0, 1]

matrix = []

for i in range(row):
    line=[]
    for j in range(col):
        line.append(0)
    matrix.append(line)

for i in range(mine):
    while True:
        x = r.randint(0, row-1)
        y = r.randint(0, col-1)
        if matrix[x][y] == 0:
            matrix[x][y] = '*'
            break


for i in range(row):
    for j in range(col):
        count = 0

        if matrix[i][j] == '*':
            continue

        for z in dk:
            for x in dk:
                c, v = i + z, j + x
                if c < 0 or v < 0 or c >= col or v >= row:
                    continue
                if matrix[c][v] == '*':
                    count += 1

        matrix[i][j] = count

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end='')
    print()