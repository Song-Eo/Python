class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self): return self.top == None

    def clear(self): self.top = None

    def push(self, item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg='LinkedStack:'):
        print(msg, end="")
        node = self.top
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None   #LinkedList 비어있는지 확인

    def clear(self): self.head = None     #LinkedList 연결 끊기(모든 노드 제거)

    def sum(self):
        node = self.head
        sum = 0
        while not node == None:
            sum += node.data
            node = node.link
        return sum

    def size(self):   #LinkedList 사이즈 확인
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg = 'LinkedList:'):    #LinkedList 출력
        print(msg, end='')
        node = self.head
        while not node == None:
            if node.link == None:
                print(node.data, end='')
            else:
                print(node.data, end='->')
            node = node.link
        print()

    def getNode(self, pos): #해당위치 노드 얻기
        if pos<0 : return None
        node = self.head;
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos): #해당위치 데이타 값 얻기
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def replace(self,pos, elem):    #해당위치 노드 얻어서 안에 데이터값 변경
        node = self.getNode(pos)
        if not node == None: node.data = elem

    def find(self, data):
        count = 0
        node = self.head
        while not node == None:
            if node.data == data: count += 1
            node = node.link
        return count

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None: # 앞에 노드가 비어있는 경우 즉, 맨 앞에 넣는 경우
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if not self.head == None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    def merge(self, listB):
        if (type(listB) == type(self)):
            while not listB.isEmpty():
                self.insert(self.size(), listB.getEntry(0))
                listB.delete(0)
        else:
            return False

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self): return self.tail == None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data  #원형 구조이기 때문에 self.tail.link가 맨 앞의 노드이다.

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
           data = self.tail.link.data
           if self.tail.link == self.tail:
               self.tail = None
           else:
               self.tail.link = self.tail.link.link
           return data

    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count

    def display(self, msg='CircularLinkedQueue: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end='->')
                node = node.link
            print(node.data, end = '->None')
        print()

class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDequq:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): return self.front == None
    def clear(self): self.front = self.rear = None
    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.front
            while not node == self.rear:
                node = node.link
                count += 1
            return count

    def display(self, msg='DoublyLinkedDeque'):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end = ' ')
        print()

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        data = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.rear = None
        else:
            self.front.prev = None
        return data

    def deleteRear(self):
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear == None:
            self.front = None
        else:
            self.rear.next = None
        return data
