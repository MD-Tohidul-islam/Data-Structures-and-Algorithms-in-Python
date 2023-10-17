from QueueLinkedList import Queue as q
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
def preorderTraveseBST(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraveseBST(rootNode.leftchild)
    preorderTraveseBST(rootNode.rightchild)
def inorderTraveseBST(rootNode):
    if not rootNode:
        return

    inorderTraveseBST(rootNode.leftchild)
    print(rootNode.data)
    inorderTraveseBST(rootNode.rightchild)
def postorderTraveseBST(rootNode):
    if not rootNode:
        return

    postorderTraveseBST(rootNode.leftchild)
    postorderTraveseBST(rootNode.rightchild)
    print(rootNode.data)

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
# print(newBST.data)
# print(newBST.leftchild.data)
# print(preorderTraveseBST(newBST))
# print(inorderTraveseBST(newBST))
#
levelorderTraversal(newBST)
