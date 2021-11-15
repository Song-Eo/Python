class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, location, a):
        lst2 = self.items[location-1:]
        self.items = self.items[:location-1]
        self.items.append(a)
        self.items = self.items + lst2

    def delete(self, location):
        lst2 = self.items[location:]
        self.items = self.items[:location]
        self.items.pop(-1)
        self.items = self.items + lst2

    def find(self, item):
        for i in range(len(self.items)):
            if(item == self.items[i]):
                return i

        return "No item"

    def merge(self, lst2):
        self.items += lst2

    def size(self):
        return len(self.items)

    def getEntry(self, pos):
        return self.items[pos]

def myLineEditor():
    list = ArrayList()
    while True:
        command = input()
        if command == 'l':
            filename = input("파일 이름: ")
            infile = open(filename, "r")
            lines = infile.readlines()
            for line in lines:
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()
        elif command == 's':
            filename = input("파일 이름: ")
            outfile = open(filename, "w")
            for i in range(list.size()):
                outfile.write(list.getEntry(i)+'\n')
            outfile.close()
        elif command == 'f':
            string = input("찾을 문자열: ")
            for i in range(list.size()):
                if string in list.getEntry(i):
                    print('[%2d]'%i, end='')
                    print(list.getEntry(i))
                
        elif command == 'p':
            print('Line Editor')
            for line in range(list.size()):
                print('[%2d]'%line, end='')
                print(list.getEntry(line))
myLineEditor()
