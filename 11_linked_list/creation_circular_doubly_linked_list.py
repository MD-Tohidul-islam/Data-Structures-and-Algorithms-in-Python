class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node == self.tail.next:
                break

    # creation of circular doubly linked list
    def createCDLl(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        newnode.next = newnode
        newnode.prev = newnode
        return 'The CDLL is created successfully'

circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLl(5))
print([node.value for node in circularDLL])

