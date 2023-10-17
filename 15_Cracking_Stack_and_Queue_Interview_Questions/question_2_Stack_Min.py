"""how would you design a stack which, in addition to push and pop,
 has a function mim which returns the minimum element? push, pop and min should all
 operate in O(1) """
class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next :
            string +=','+str(self.next)
        return string

class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self, value):
        if self.minNode and (self.minNode.value < value):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value = value, next=self.minNode)
        self.top = Node(value = value , next= self.top)
    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item
customstack = Stack()
customstack.push(5)
print(customstack.min())
customstack.push(6)
print(customstack.min())
customstack.push(4)
print(customstack.min())
customstack.push(3)
print(customstack.min())
customstack.pop()
print(customstack.min())
