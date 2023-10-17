#   Created by Elshad Karimov on 12/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Node:
    def __init__(self, value=None):
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
            node = node.next
            if node == self.tail.next:
                break

    #  Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"

    # Insertion Method in Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"


    def deletionCDLL(self,location):
        if self.head is None:
            return 'there is no element to delete'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                curnode = self.head
                index = 0
                while index < location-1:
                    curnode = curnode.next
                    index +=1
                curnode.next = curnode.next.next
                curnode.next.prev = curnode
            print('the node has been successfully deleted')

    # delete the entire circular doubly linked list
    def deleteEntireCDLL(self):
        if self.head is None:
            print('there is not any element to delete')
        else:
            self.tail.next = None
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print('the entire circular doubly linked list is deleted')




circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.insertCDLL(3,0)
circularDLL.insertCDLL(5,1)
circularDLL.insertCDLL(7,2)
print([node.value for node in circularDLL])
circularDLL.deletionCDLL(0)
print([node.value for node in circularDLL])
circularDLL.deletionCDLL(1)
print([node.value for node in circularDLL])
circularDLL.deletionCDLL(2)
print([node.value for node in circularDLL])
circularDLL.deleteEntireCDLL()
print([node.value for node in circularDLL])

