class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Tree:
    def __init__(self):
        self.root=None






def sumchid(root):
    if root.left  is  None or root.right is None:
        return 0
    

    if root.left.data+root.right.data==root.data:
        sumchid(root.left)
        sumchid(root.right)
        return True
    
    return False





n1=Node(10)
t1=Tree()
t1.root=n1
n1.left=Node(4)
n1.right=Node(6)
n1.left.left=Node(1)
n1.left.right=Node(3)
n1.right.left=Node(8)
n1.right.right=Node(4)




print(sumchid(t1.root))