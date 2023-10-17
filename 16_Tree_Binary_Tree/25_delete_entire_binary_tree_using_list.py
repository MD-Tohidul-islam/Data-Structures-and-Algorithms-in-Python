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
    def levelorderTraversal(self, index):
        for i in range(index, self.lastusedindex+1):
            print(self.customList[i])

    def deleteBT(self):
        self.customList = None
        return 'The binary tree is successfully deleted'

newbinarytree = BinaryTree(8)
print(newbinarytree.insertNode('Drinks'))
print(newbinarytree.insertNode('hot'))
print(newbinarytree.insertNode('cold'))
print(newbinarytree.insertNode('tea'))
print(newbinarytree.insertNode('water'))
newbinarytree.deleteBT('tea')
print(newbinarytree.levelorderTraversal(1))