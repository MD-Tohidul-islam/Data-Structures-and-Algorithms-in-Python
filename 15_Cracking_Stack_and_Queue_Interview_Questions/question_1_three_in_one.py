# use a single list to implement three stacks.

class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custlist = [0]* (stacksize*self.numberstacks)
        self.sizes = [0]*self.numberstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    def isEmpty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    def indexofTop(self,stacknum):
        offset = stacknum*self.stacksize
        return offset+ self.sizes[stacknum]-1

    def push(self,item, stacknum):
        if self.isFull(stacknum):
            return 'The stack is full'
        else:
            self.sizes[stacknum] +=1
            self.custlist[self.indexofTop(stacknum)] = item
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else:
            value = self.custlist[self.indexofTop(stacknum)]
            self.custlist[self.indexofTop(stacknum)] = 0
            self.sizes[stacknum] -=1
            return value

    def peek(self, stacknum):

        if self.isEmpty(stacknum):
            return 'The stack is empty'
        else:
            value = self.custlist[self.indexofTop(stacknum)]
            return value
customstack = MultiStack(6)
print(customstack.isFull(0))
print(customstack.isFull(1))
customstack.push(1,0)
customstack.push(2,0)
customstack.push(3,2)
print(customstack)
print(customstack.peek(1))

