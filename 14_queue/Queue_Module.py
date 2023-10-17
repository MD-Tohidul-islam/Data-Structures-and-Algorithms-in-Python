import queue as q
customqueue = q.Queue(maxsize=3)

print(customqueue.qsize())

print(customqueue.empty())
customqueue.put(1)
customqueue.put(2)
customqueue.put(3)
print(customqueue.qsize())
print(customqueue)
print(customqueue.full())
print(customqueue.get())
print(customqueue.qsize())
