# class node
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

singly_linked_list = SlinkedList()
node1 = Node(1)
node2 = Node(2)

singly_linked_list.head = node1
singly_linked_list.head.next = node2
singly_linked_list.tail = node2
