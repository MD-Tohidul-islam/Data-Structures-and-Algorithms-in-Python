class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

newtree = TreeNode('Drinks')
lchild = TreeNode('hot')
tea = TreeNode('tea')
coffee = TreeNode('coffee')
lchild.leftchild = tea
lchild.rightchild = coffee
rchild = TreeNode('cold')
newtree.leftchild = lchild
newtree.rightchild= rchild


def inordertraversal(rootNode):
    if not rootNode:
        return

    inordertraversal(rootNode.leftchild)
    inordertraversal(rootNode.rightchild)
    print(rootNode.data)
inordertraversal(newtree)