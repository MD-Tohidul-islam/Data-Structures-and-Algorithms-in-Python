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
                newNode.next = self.tail.next


            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode


    # searching for a node in circular singly linked list
    def searchCSLl(self, value):
        if self.head is None:
            return 'the linked list dose not exits'
        else:
            tempnode = self.head
            while tempnode :
                if tempnode.value == value:
                    return 'the value is find'
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break
            return 'the value is not in the list'


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
print([node.value for node in circularSll])
print(circularSll.searchCSLl(12))