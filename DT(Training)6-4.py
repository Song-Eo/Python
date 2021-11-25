class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoubleLinkedList:  #이중연결리스트
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): return self.rear == None

    def push(self, item):
        node = DNode(item)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node

    def pop(self):
        if not self.isEmpty():
            node = self.front
            self.front = self.front.next
            n = node.data
            node.link = None
            return n
        else:
            return False

    def display(self, msg='DoubleLinkedList: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end='<->')
                node = node.next
            print(node.data, end='->None')
        print()

dl = DoubleLinkedList(); dl.push(3); dl.push(6); dl.push(7)
dl.push(9); dl.display(); dl.pop(); dl.display()
