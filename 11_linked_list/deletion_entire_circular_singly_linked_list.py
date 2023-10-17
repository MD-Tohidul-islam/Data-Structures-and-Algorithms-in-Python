class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next


    # Creation of circular singly linked list

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return 'the circular singly linked list is created'

    #  insertion in circular singly linked list
    def insertCSLL(self, value, location):
        if self.head is None:
            return "the head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                # newNode.next = self.tail.next
                # self.tail.next = newNode
                # self.tail = newNode
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = self.head


            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # delete entire circular singly linked list
    def deleteEnireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

circularSll = CircularSinglyLinkedList()
circularSll.createCSLL(1)
print([node.value for node in circularSll])
circularSll.insertCSLL(0,0)
print([node.value for node in circularSll])
circularSll.insertCSLL(2,1)
print([node.value for node in circularSll])
circularSll.insertCSLL(3,1)
print([node.value for node in circularSll])
circularSll.insertCSLL(4,2)
print([node.value for node in circularSll])
circularSll.insertCSLL(5,1)
circularSll.deleteEnireCSLL()
print([node.value for node in circularSll])

