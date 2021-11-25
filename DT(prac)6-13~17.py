from Python.Data_structure.ADT_LinkedStructure import LinkedList

ll = LinkedList()
num = int(input("노드의 개수: "))
for i in range(num):
    value = int(input("노드 #%d 데이터 : "%(i+1)))
    ll.insert(i,value)
value = int(input("끝에 추가할 데이터: "))
ll.insert(num,value)
ll.display()
ll.delete(0)
print("첫 번째 노드 삭제 후 연결 리스트: ", end = '')
ll.display()
print("연결 리스트의 데이터 합: ", ll.sum())
f = int(input("탐색할 값을 입력하세요: "))
print("%d는 연결 리스트에서 %d번 나타납니다."%(f,ll.find(f)))