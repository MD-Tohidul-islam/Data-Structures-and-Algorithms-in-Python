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


def searchNode(rootNode, nodevalue):
    if rootNode.data == nodevalue:
        print('The value is found')
    elif nodevalue < rootNode.data:
        if rootNode.leftchild.data == nodevalue:
            print('The value is found')
        else:
            searchNode(rootNode.leftchild, nodevalue)
    else:
        if rootNode.rightchild.data == nodevalue:
            print('The value is found')
        else:
            searchNode(rootNode.rightchild, nodevalue)


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

searchNode(newBST,40)