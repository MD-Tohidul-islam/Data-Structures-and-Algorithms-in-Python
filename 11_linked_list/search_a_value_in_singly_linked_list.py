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

    # traversal singly linked list
    def traversalSLL(self):
        if self.head is None:
            print('the singly linked list dose not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # search for a value in singly linked list
    def searchSLL(self, nodeValue):
        if self.head is None:
            return 'the list does not exist'
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return 'The value does not exist in this list'
singlyLinkedLins = SlinkedList()
singlyLinkedLins.insertSLL(1,0)
singlyLinkedLins.insertSLL(1,1)
singlyLinkedLins.insertSLL(3,1)
singlyLinkedLins.insertSLL(4,1)
singlyLinkedLins.insertSLL(1,0)
singlyLinkedLins.insertSLL(9,3)
print([node.value for node in singlyLinkedLins])
#singlyLinkedLins.traversalSLL()
print(singlyLinkedLins.searchSLL(10))
print(singlyLinkedLins.searchSLL(3))