class Node:
    def __del__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curnode = self.head
        while curnode:
            yield curnode
            curnode = curnode.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        newnode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newnode
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode
    def isEmpty(self):
        if self.linkedlist.head == None :
            return True
        else:
            return False


    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            temnode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return temnode
    def peek(self):
        if self.isEmpty():
            return 'the queue is empty'
        else:
            return self.linkedlist.head
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


customqueue = Queue()
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
customqueue.enqueue(4)
print(customqueue)
