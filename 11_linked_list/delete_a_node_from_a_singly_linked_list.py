# class node
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


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
                newNode.next = self.head
                self.head = newNode

            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    #  Delete a node form singly linked list

    def deleteNode(self,location):
        if self.head is None:
            return 'the list does not exist'
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None :
                        if  node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next





singlyLinkedLins = SlinkedList()
singlyLinkedLins.insertSLL(1,0)
singlyLinkedLins.insertSLL(1,1)
singlyLinkedLins.insertSLL(3,1)
singlyLinkedLins.insertSLL(4,1)
singlyLinkedLins.insertSLL(1,0)
singlyLinkedLins.insertSLL(9,3)
print([node.value for node in singlyLinkedLins])
#singlyLinkedLins.traversalSLL()
# print(singlyLinkedLins.searchSLL(10))
singlyLinkedLins.deleteNode(1)
print([node.value for node in singlyLinkedLins])