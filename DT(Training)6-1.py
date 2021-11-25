from Python.Data_structure.ADT_LinkedStructure import LinkedStack

ls = LinkedStack()
flag = 1
data = input("알고 싶은 회문은? : ")
cData = ''.join(c for c in data if data.isalnum)

if ( len(cData) % 2 == 1 ):
    middle = len(cData)//2
    data = cData[:middle]
    cData = cData[middle+1:]

for i in range(len(data)):
    ls.push(data[i])

for i in cData:
    if ls.pop() != i:
        flag = 0
        break

if flag == 1:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
