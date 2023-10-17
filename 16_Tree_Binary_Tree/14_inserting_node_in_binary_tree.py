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

def insertNodeBT(rootNode, newvaleu):
    if not rootNode:
        rootNode = newvaleu
    else:
        cusQ = q.Queue()
        cusQ.enqueue(rootNode)
        while not (cusQ.isEmpty()):
            root = cusQ.dequeue()
            if root.value.leftChild is not None:
                cusQ.enqueue(root.value.leftChild)
            else:
                root.value.rightChild = newvaleu
                return 'Successfully inserted'
            if root.value.rightChild is not None:
                cusQ.enqueue(root.value.rightChild)
            else:
                root.value.reftChild = newvaleu
                return 'Successfully inserted'
newNode = TreeNode('cola')
insertNodeBT(newBT,newNode)
