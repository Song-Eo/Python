n = int(input())
data = list(map(int, input().split()))
if n == 1:
    print('A')

elif n == 2:
    if data[0] == data[1]:
        print(data[0])
    else:
        print('A')

else:
    if data[0] == data[1]:
        a = 0
    else:
        a = (data[1] - data[2]) // (data[0] - data[1])
    b = data[2] - data[1]*a
    for i in range(n-1):
        if data[i+1] != data[i]*a+b:
            total = 'B'
            break
        else:
            total = data[n-1]*a+b

    print(total)