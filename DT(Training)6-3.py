class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link

class LinkedQueue:  #연결된 큐리스트
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self): return self.rear == None

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if not self.isEmpty():
            node = self.front
            self.front = self.front.link
            n = node.data
            node.link = None
            return n
        else:
            return False

    def display(self, msg='LinkedQueue: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end='->')
                node = node.link
            print(node.data, end='->None')
        print()

lq = LinkedQueue(); lq.enqueue(3); lq.enqueue(4); lq.enqueue(5) ;lq.enqueue(6)
lq.display(); lq.dequeue(); lq.display()

