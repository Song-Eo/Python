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
        
    
def checkBrackets(lines):
    stack = Stack()
    for line in lines:
        for ch in line:
            if stack.peek() not in ('"', '\'', '#'):
                if ch in ('{', '[', '(', '"', '\'', '#'):
                    stack.push(ch)
                elif ch in ('}', ']', ')'):
                    if stack.isEmpty():
                        return False
                    else:
                        left = stack.pop()
                        if(ch == "}" and left != "{") or\
                          (ch == "]" and left != "[") or\
                          (ch == ")" and left != "("):
                            return False
            elif ch in ('\'', '"') and stack.peek() in ('"', '\''):
                stack.pop()
            else:
                continue
        if stack.peek() == '#':
            stack.pop()
    return stack.isEmpty()

filename = "js.txt"
infile = open(filename, "r")
lines = infile.readlines()
infile.close

result = checkBrackets(lines)
print(filename, "--->", result)
