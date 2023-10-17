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

newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 60))
print(newBST.data)
print(newBST.leftchild.data)
