class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    


def preorder(root):
    if not root:
        return
    print(root.data,end="->")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end="->")
    inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end="->")

node1=Node(10)
node1.left=Node(20)
node1.right=Node(30)
node1.left.left=Node(40)
node1.left.right=Node(50)
node1.right.left=Node(60)
node1.right.right=Node(70)

preorder(node1)
print()
inorder(node1)
print()
postorder(node1)
