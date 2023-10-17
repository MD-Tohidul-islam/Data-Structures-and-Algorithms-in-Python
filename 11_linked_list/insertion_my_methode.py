class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in linked list
    def insertSLL(self,value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                self.head = newNode
                newNode.next = self.tail
            elif location == 1:
                self.tail.next = newNode
                newNode.next = None
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode





singlyLinkedLins = SlinkedList()
singlyLinkedLins.insertSLL(1,0)
singlyLinkedLins.insertSLL(2,1)
singlyLinkedLins.insertSLL(3,1)
singlyLinkedLins.insertSLL(5,2)
singlyLinkedLins.insertSLL(6,3)
singlyLinkedLins.insertSLL(7,4)
singlyLinkedLins.insertSLL(8,5)
print([node.value for node in singlyLinkedLins])