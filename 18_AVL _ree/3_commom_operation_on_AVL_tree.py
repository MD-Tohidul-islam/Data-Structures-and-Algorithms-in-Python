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

