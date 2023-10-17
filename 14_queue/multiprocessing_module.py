from multiprocessing import Queue

customqueue = Queue(maxsize=3)
print(customqueue)
customqueue.put(1)
customqueue.put(2)
customqueue.put(3)
print(customqueue.get())