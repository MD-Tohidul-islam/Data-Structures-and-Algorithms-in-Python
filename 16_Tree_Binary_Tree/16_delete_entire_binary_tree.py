import q


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


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customq = q.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            if root.value.leftChild is not None:
                customq.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customq.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customq = q.Queue()
        customq.enqueue(rootNode)
        while not (customq.isEmpty()):
            root = customq.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customq.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customq.enqueue(root.value.leftChild)


# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT,newNode)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return 'The BT does not exist'
    else:
        customq = q.Queue()
        customq.enqueue(rootNode)
        while not customq.isEmpty():
            root = customq.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return 'The node has been deleted'
            if root.value.leftChild is not None:
                customq.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customq.enqueue(root.value.rightChild)
        return 'Failed to delete'


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
deleteBT(newBT)

