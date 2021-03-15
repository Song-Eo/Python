time, win = map(int, input().split())
rate = int((win/time) * 100)
count = 0

if rate >= 99:
    count = -1

else:
    while True:
        count += 1
        time += 1
        win += 1
        if rate != int((win/time) * 100):
            break

print(count)