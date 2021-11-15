class Set:
    def __init__(self):
        self.items=[]

    def size(self):
        return len(self.items)
    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return True
        return False
    def delete(self, item):
        if self.contains(item):
            if self.items[len(self.items)-1] == item:
                self.items.pop()
            else:
                for i in range(len(self.items)):
                    if self.items[i] == item:
                        lst = self.items[i+1:]
                        self.items = self.items[:i+1]
                        self.items.pop()
                        self.items += lst
                        break
                    
    def insert(self, item):
        if not self.contains(item):
            self.items.append(item)

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for i in setB.items:
            if not self.contains(i):
                setC.items.append(i)
        return setC
    
    def intersect(self, setB):
        setC = Set()
        for i in setB.items:
            if self.contains(i):
                setC.items.append(i)
        return setC

    def defference(self, setB):
        setC = Set()
        for i in self.items:
            if not setB.contains(i):
                setC.items.append(i)
        return setC

    def __sub__(self, setB):
        setC = Set()
        for i in self.items:
            if not setB.contains(i):
                setC.items.append(i)
        return setC

    def isSubsetOf(self, setB):
        for i in self.items:
            if not setB.contains(i):
                return False
        return True
    
a = Set()
b = Set()
a.items = [3,6,9]
b.items = [3,6,9,12]
print(a.isSubsetOf(b))        
