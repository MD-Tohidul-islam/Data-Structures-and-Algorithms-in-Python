class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    # is full
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
    # push
    def push(self, value):
        if self.isFull():
            return 'The stack is full'
        else:
            self.list.append(value)
            return 'The element has been successfully inserted'

    # pop
    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return 'there is not any element to peek'
        else:
            return self.list[len(self.list) - 1]

    # delete
    def delete(self):
        self.list = None

customStack = Stack(12)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(6)
#print(customStack)
customStack.pop()
customStack.peek()
print(customStack)