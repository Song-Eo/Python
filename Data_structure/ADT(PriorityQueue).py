class PriorityQueue:
    def __init__(self):
        self.items= []

    def isEmpty(self):
        return len(self.items) == 0

    def sort(self):
        for i in range(len(self.items)-1, 0, -1):
            if self.items[i] > self.items[i-1]:
                self.items[i], self.items[i - 1] = self.items[i-1], self.items[i]

    def enqueue(self, item):
        self.items.append(item)
        self.sort()

    def dequeue(self):
        if not self.isEmpty():
            s = self.items[0]
            del(self.items[0])
            return s
        return False

    def peek(self):
        if not self.isEmpty():
            return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def display(self):
        print(self.items)

que = PriorityQueue()

que.enqueue(4)
que.enqueue(9)
que.enqueue(2)
que.enqueue(14)

que.display()


