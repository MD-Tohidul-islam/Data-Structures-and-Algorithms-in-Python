class Node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    # creation of doubly linked list
    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The DLL is created successfully'

    #  Insertion method in doubly linked list
    def insertNode(self, value, location):
        if self.head is None:
            return 'the node cannot be inserted'
        else:
            newnode = Node(value)
            if location == 0:
                newnode.prev = None
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif location == 1:
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                tempnode.next.prev = newnode
                tempnode.next = newnode

    # delete entire doubly linked list
    def deleteDLl(self):
        if self.head is None:
            print('There is not any node in DLl')
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print('the DLL has been deleted')


doublyLl = DoublyLinkedList()
doublyLl.createDLL(5)
print([node.value for node in doublyLl])
doublyLl.insertNode(0,0)
doublyLl.insertNode(2,1)
doublyLl.insertNode(3,1)
doublyLl.insertNode(4,1)
doublyLl.insertNode(5,1)
doublyLl.insertNode(6,1)
doublyLl.insertNode(7,1)
doublyLl.insertNode(8,1)


print([node.value for node in doublyLl])
doublyLl.deleteDLl()
print([node.value for node in doublyLl])