class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

newtree = TreeNode('Drinks')
lchild = TreeNode('hot')
rchild = TreeNode('cold')
newtree.leftchild = lchild
newtree.rightchild= rchild

def inordertraversal(rootNode):
    if not rootNode:
        return

    inordertraversal(rootNode.leftchild)
    print(rootNode.data)
    inordertraversal(rootNode.rightchild)
inordertraversal(newtree)