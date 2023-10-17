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

def preordertraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preordertraversal(rootNode.leftchild)
    preordertraversal(rootNode.rightchild)
preordertraversal(newtree)

