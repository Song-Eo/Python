from Python.Data_structure.ADT_LinkedStructure import CircularLinkedQueue

lq = CircularLinkedQueue()

while True:
    value = int(input("양의 정수를 입력하세요(종료: -1): "))
    if value == -1:
        break
    lq.enqueue(value)
lq.display()



