class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertNode(rootNode, nodevalue):
    if rootNode.data == None:
        rootNode.data = nodevalue
    elif nodevalue <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(nodevalue)
        else:
            insertNode(rootNode.leftchild, nodevalue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(nodevalue)
        else:
            insertNode(rootNode.rightchild, nodevalue)
    return 'The node has been successfully inserted'

# find minimum value
def minvalueNode(bstNode):
    current = bstNode
    while (current.leftchild is not None):
        current.leftchild
    return current

def deleteNode(rootNode, nodevalue):
    if rootNode is None:
        return rootNode
    if nodevalue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, nodevalue)
    elif nodevalue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild, nodevalue)
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild
            rootNode = None
            return temp
        if rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
        temp = minvalueNode(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild, temp.data)
    return rootNode
from QueueLinkedList import Queue as q
def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQ =q()
        customQ.enqueue(rootNode)
        while not (customQ.isEmpty()):
            root = customQ.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQ.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQ.enqueue(root.value.rightchild)
newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))

deleteNode(newBST,20)
print(levelorderTraversal(newBST))