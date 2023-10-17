import QueueLinkedList as q
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


newAVL = AVLNode(10)


def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)


def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)


def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)
    postorderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        custom_q = q.Queue()
        custom_q.enqueue(rootNode)
        while not custom_q.isEmpty():
            root = custom_q.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                custom_q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custom_q.enqueue(root.value.rightChild)

def searchNode(rootNode, nodevalue):
    if rootNode.data == nodevalue:
        print('The value is found')
    elif nodevalue < rootNode.data:
        if rootNode.leftChild.data == nodevalue:
            print('The value is found')
        else:
            searchNode(rootNode.leftChild, nodevalue)
    elif nodevalue > rootNode.data:
        if rootNode.rightChild.data == nodevalue:
            print('The value is found')
        else:
            searchNode(rootNode.rightChild, nodevalue)
    else:
        print('The value is not found')

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotation(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChil))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChil))
    return newRoot

def leftRotation(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild),getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)
    if balance >1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not  rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0 :
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance > -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode



newAVL = AVLNode(5)
newAVL = insertNode(newAVL,10)
newAVL = insertNode(newAVL,15)
newAVL = insertNode(newAVL,20)
newAVL = deleteNode(newAVL,15)
levelorderTraversal(newAVL)






