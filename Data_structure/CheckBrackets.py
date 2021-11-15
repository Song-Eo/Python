class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self):self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        
    
def checkBracketsV2(lines):
    stack = Stack()
    countline = 0
    for line in lines:
        countline += 1
        countchar = 0
        for ch in line:
            countchar += 1
            if ch in ('{', '[', '('):
                stack.push(ch)
            elif ch in ('}', ']', ')'):
                if stack.isEmpty():
                    error = "Error : 2번 조건 위반 " + str(countline) +"줄 " + str(countchar) + "번째"
                    return error
                else:
                    left = stack.pop()
                    if(ch == "}" and left != "{") or\
                      (ch == "]" and left != "[") or\
                      (ch == ")" and left != "("):
                        error = "Error : 3번 조건 위반" + str(countline) +"줄 " + str(countchar) + "번째"
                        return error

    if stack.isEmpty(): return '0'
    else:
        error = "Error : 1번 조건 위반" + str(countline) +"줄 " + str(countchar) + "번째"
        return error

filename = input("파일이름입력(바이너리파일): ")
infile = open(filename, "rb")
blines = infile.readlines();
infile.close()

lines = []
for i in blines:
    lines.append(str(i, 'utf-8'))
    

result = checkBracketsV2(lines)
print(filename, "-->", result)
