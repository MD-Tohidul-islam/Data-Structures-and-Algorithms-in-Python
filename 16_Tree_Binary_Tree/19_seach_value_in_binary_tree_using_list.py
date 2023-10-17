class BinaryTree:
    def __init__(self,size):
        self.customList = size*[None]
        self.lastusedindex = 0
        self.maxsize = size

    def insertNode(self,value):
        if self.lastusedindex +1 == self.maxsize:
            return 'The Binary Tree is full'
        self.customList[self.lastusedindex+1] = value
        self.lastusedindex +=1
        return 'The value has been successfully inserted'

    def searchNode(self,nodevalue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodevalue:
                return 'Success'
        return 'Not found'



newbinarytree = BinaryTree(8)
print(newbinarytree.insertNode('Drinks'))
print(newbinarytree.insertNode('tea'))
print(newbinarytree.insertNode('water'))
print(newbinarytree.searchNode('hot'))
print(newbinarytree.searchNode('tea'))
