import queue


def isVaildPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def DFS():
    S = queue.LifoQueue(maxsize=10)
    S.put((0, 1))
    print('DFS :')

    while not S.empty():
        here = S.get()
        print(here, end=" -> ")
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isVaildPos(x, y - 1): S.put((x, y - 1))
            if isVaildPos(x, y + 1): S.put((x, y + 1))
            if isVaildPos(x - 1, y): S.put((x - 1, y))
            if isVaildPos(x + 1, y): S.put((x + 1, y))
    return False


def BFS():
    Q = queue.Queue(maxsize=10)
    Q.put((0, 1))
    print('BFS: ')

    while not Q.empty():
        here = Q.get()
        print(here, end=" -> ")
        x, y = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isVaildPos(x, y - 1): Q.put((x, y - 1))
            if isVaildPos(x, y + 1): Q.put((x, y + 1))
            if isVaildPos(x - 1, y): Q.put((x - 1, y))
            if isVaildPos(x + 1, y): Q.put((x + 1, y))
    return False


map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6

result = DFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')

map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]

result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')


