class Queue:
    def __init__(self, maxsize):
        self.itmes = maxsize *[None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.itmes]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return 'The queue is full'
        else:
            if self.top+1 == self.maxsize:
                self.top = 0
            else:
                self.top+=1
                if self.start == -1:
                    self.start = 0
        self.itmes[self.top] = value
        return 'the element is inserted at the end of Queue'

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            firstelement = self.itmes[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start +1 == self.maxsize:
                self.start = 0
            else:
                self.start +=1
            self.itmes[start] = None
            return firstelement
    def peek(self):
        if self.isEmpty():
            return 'the queue is empty'
        else:
            return self.itmes[self.start]

    def delete(self):
        self.itmes = self.maxsize *[None]
        self.top = -1
        self.start = -1






customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)

