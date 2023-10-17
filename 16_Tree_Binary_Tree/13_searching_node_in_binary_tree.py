import  q
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = q.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
#levelOrderTraversal(newBT)

def searchBT(rootnode, nodevalue):
    if not rootnode:
        return 'the binary tree does not extst'
    else:
        customQueur = q.Queue()
        customQueur.enqueue(rootnode)
        while not (customQueur.isEmpty()):
            root = customQueur.dequeue()
            if root.value.data == nodevalue:
                return 'Success'
            if (root.value.leftChild is not None):
                customQueur.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueur.enqueue(root.value.rightChild)

        return 'the value does not find'

print(searchBT(newBT,'Tea'))



