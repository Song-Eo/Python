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

def precedence(op):
    if op=='(' or op==')' : return 0
    elif op=='+' or op=='-' : return 1
    elif op=='*' or op=='/' : return 2
    else : return -1

def infix2Postfix(expr):
    s = Stack()
    output = []
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op=='(' : break;
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op=s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output

def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()

infix = input("수식입력: ")
postfix = infix2Postfix(infix)
result = evalPostfix(postfix)
print("중위표기: ", infix)
print("후위표기: ", postfix)
print("계산결과: ", result)
