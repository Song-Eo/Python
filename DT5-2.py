import queue   #스택 2개로 큐 구현

s1 = queue.LifoQueue(maxsize=10)
s2 = queue.LifoQueue(maxsize=10)

while True:
    sel = int(input("1. 입력, 2. 출력, 3. 종료"))
    if (sel==1):
        item = input("입력하세요: ")
        s1.put(item)

    elif (sel==2):
        while not s1.empty():
            s2.put(s1.get())

        while not s2.empty():
            print(s2.get())

    elif (sel==3):
        print("종료합니다")
        break
    else:
        print("잘못된 입력입니다.")