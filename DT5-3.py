import queue
def fibo(n):
    que = queue.Queue(maxsize=20)
    que.put(0); que.put(1)
    for i in range(n-1):
        a = que.get(); b = que.get()
        c = a + b
        que.put(b); que.put(c)
    que.get()
    return que.get()

print(fibo(8))
