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

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return 'the BST has been successfully deleted'
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
deleteBST(newBST)