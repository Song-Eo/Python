class Node:
    def __init__(self, elem, link = None):
        self.data = elem
        self.link = link

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

